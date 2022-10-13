# App Version
version="1.0.0"

cd ..

# Build the Mac version
pipenv run exportmac

cd dist
mkdir PDF-Ripper-$version

mv PDF-Ripper.app PDF-Ripper-$version/PDF-Ripper.app

# Create the DMG
hdiutil create -srcfolder PDF-Ripper-$version -volname PDF-Ripper-$version PDF-Ripper-$version.dmg

# Move the DMG to the GitHub docs downloads folder
cd ..
mv ./dist/PDF-Ripper-$version.dmg ./docs/downloads/mac/PDF-Ripper-$version.dmg

# Clean up
rm -rf ./dist
rm -rf ./Build
rm PDF-Ripper.spec
