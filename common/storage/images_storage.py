from ftplib import FTP

ftp = FTP('braderhut.netne.net')


def start():
    ftp.login(user='a1634887', passwd='qwerty7890')
    ftp.cwd('public_html/images')


def stop():
    ftp.quit()


def save_image(imagename, file):
    ftp.storlines('STOR ' + str(imagename), file)
