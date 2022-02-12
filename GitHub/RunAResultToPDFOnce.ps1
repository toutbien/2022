#Enable print to PDF feature from PWSH:
Enable-WindowsOptionalFeature -Online -FeatureName Printing-PrintToPDFServices-Features 

#verify you are ready to print
#$printer = Get-Printer -Name "Microsoft Print to PDF" -ErrorAction SilentlyContinue
#if (!$?)
#{
#    Write-Warning "Your PDF Printer is not yet available!"
#}
#else
#{
#    Write-Warning "PDF printer is ready for use."
#}

#Create a PDF only printer for output files using a port
    # choose a name for your new printer
$printerName = 'PrintToPDF'
    # choose a default path where the PDF is saved
$PDFFilePath = "$env:temp\PDFResultFile.pdf"
    # choose whether you want to print a test page
#$TestPage = $true

#see whether the driver exists
$ok = @(Get-PrinterDriver -Name "Microsoft Print to PDF" -ea 0).Count -gt 0
if (!$ok)
{
    Write-Warning "Printer driver 'Microsoft Print to PDF' not available."
    Write-Warning "This driver ships with Windows 10 or Windows Server 2016."
    Write-Warning "If it is still not available, enable the 'Printing-PrintToPDFServices-Features'"
    Write-Warning "Example: Enable-WindowsOptionalFeature -Online -FeatureName Printing-PrintToPDFServices-Features"
    return
}

# check whether port exists
$port = Get-PrinterPort -Name $PDFFilePath -ErrorAction SilentlyContinue
if ($port -eq $null)
{
    # create printer port
    Add-PrinterPort -Name $PDFFilePath 
}

# add printer -only needs to be done once during the opens session
#Add-Printer -DriverName "Microsoft Print to PDF" -Name $printerName -PortName $PDFFilePath 

# print a test page to the printer
if ($TestPage)
{
    $printerObject = Get-CimInstance Win32_Printer -Filter "name LIKE '$printerName'"
    $null = $printerObject | Invoke-CimMethod -MethodName printtestpage 
    Start-Sleep -Seconds 1
    Invoke-Item -Path $PDFFilePath
}

# specify the path to the file you want to create
$OutPath = "YOUR\PATH"

# this is the file the print driver always prints to
$TempPDF = "$env:temp\PDFResultFile.pdf"

# make sure old print results are removed
$exists = Test-Path -Path $TempPDF
if ($exists) { Remove-Item -Path $TempPDF -Force }

# send PowerShell results to PDF -adding NoClobber will ensure you arent overwriting if the last filename was not changed
Get-Service -Name Appinfo | Out-Printer -Name "PrintToPDF"

# wait for the print job to be completed, then move file
$ok = $false
do { 
    Start-Sleep -Milliseconds 500 
    Write-Host '.' -NoNewline
                
    $fileExists = Test-Path -Path $TempPDF
    if ($fileExists)
    {
        try
        {
            Move-Item -Path $TempPDF -Destination $OutPath -Force -ErrorAction Stop
            $ok = $true
        }
        catch
        {
            # file is still in use, cannot move
            # try again
        }
    }
} until ( $ok )
Write-Host

# show new PDF file in explorer
explorer "/select,$OutPath"

#Create a PDF file from PWSH through Out-Printer where you can name the file and select the location:
#Get-Service  | Out-Printer -Name "Microsoft Print to PDF"