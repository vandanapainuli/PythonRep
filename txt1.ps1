
# Define the path
$folderPath = "$env:USERPROFILE\Desktop\MyTestFolder"

# Create the folder if it doesn't exist
if (-not (Test-Path -Path $folderPath)) {
    New-Item -ItemType Directory -Path $folderPath
}

# Create a text file and write to it
$textFile = "$folderPath\hello.txt"
"Hello from PowerShell!" | Out-File -FilePath $textFile
