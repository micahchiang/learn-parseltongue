#! python3
# renames files with american date format to european date format

import shutil, os, re, zipfile

# regex that matches american date format
dataPattern = re.compile(r'''(.*?) 
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
''', re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo == None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFilename = beforePart + dayPart + '-' + monthPart + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    # shutil.move(amerFilename, euroFilename)

def backUpToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    for foldername, subfolders, filenames in os.walk(foler):
        print('Adding files in %s...' % (folername))
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')