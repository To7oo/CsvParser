param (
    [string]$carpetaOrigen,
    [string]$carpetaDestino
)

if (-not (Test-Path -Path $carpetaOrigen -PathType Container)) {
    Write-Host "La carpeta de origen no existe."
    exit
}

if (-not (Test-Path -Path $carpetaDestino -PathType Container)) {
    New-Item -Path $carpetaDestino -ItemType Directory -Force
}

$archivosZip = Get-ChildItem -Path $carpetaOrigen -Filter *.zip

# Descomprimir cada archivo .zip en la carpeta de destino
foreach ($archivoZip in $archivosZip) {

    Expand-Archive -Path $archivoZip.FullName -DestinationPath $carpetaDestino -Force
    Write-Host "Se ha descomprimido $($archivoZip.FullName) en $carpetaDestino"
}
