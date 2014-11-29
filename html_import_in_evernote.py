__author__ = 'hgp1964'
"""
I wrote a program that imports a test file wiht html links into evernote
It is a combination of python and applescript. Fill in the path  your textfile in the
main programm. It will import from the first line till the end. If you get stuck
at e.g. line 100, then alter the start line and continue importing.


if __name__ == '__main__':
    source = "path to your file"
    startline = 0
    html_list_into_evernote(source,startline)


The code is not completely foolproof. Every now and again evernote might crash. This is the
reason why I build in a while loop and provide the option to change the start line.

I have found a lot of this code online. Feel free to use and improve it.

Yours truly,

Henk


"""
import subprocess
import httplib
from urlparse import urlparse


def checkUrl(url):
    """
    http://stackoverflow.com/questions/6471275/python-script-to-see-if-a-web-page-exists-without-downloading-the-whole-page
    his will send an HTTP HEAD request and return True if the response status code is < 400.
    :param url:
    :return:
    """
    try:
        p = urlparse(url)
        conn = httplib.HTTPConnection(p.netloc)
        conn.request('HEAD', p.path)
        resp = conn.getresponse()
        return resp.status < 400
    except:
        print "fout in check url"
        return False


def asrun(ascript):
    """
    Run the given AppleScript and return the standard output and error.
    http://www.leancrew.com/all-this/2013/03/combining-python-and-applescript/
    """

    osa = subprocess.Popen(['osascript', '-'],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)
    return osa.communicate(ascript)[0]

def asquote(astr):
    """
    Return the AppleScript equivalent of the given string.
    """

    astr = astr.replace('"', '" & quote & "')
    return '"{}"'.format(astr)

def create_evernote_note_from_url(title,url):
    """
    The function creates a note from the given in the notebook test
    You can easily change this


    The option to create a tag has been commented out

    """
    ascript = '''
    tell application id "com.evernote.evernote"
        try
            set myNotebook to notebook "test"
            set mynote to create note title {0} from url {1} notebook name of myNotebook
            # set tag1 to tag "proef tag"
            # assign tag1 to mynote
            delay 3
            close window 1
            return mynote
        on error number num
            return "error"
        end try
    end tell'''.format(asquote(title), asquote(url))

    response = asrun(ascript)
    return response

def html_list_into_evernote(sourcefile, startline):
    """
    This function was tested
    :return:
    """

    myfile = sourcefile


    with open(myfile) as f:
        content = f.readlines()

    number_of_records = len(content)
    print "number of lines is ", str(number_of_records)

    # the counter cntr is used to keep track of your imports
    cntr = startline
    print startline

    while cntr < number_of_records:
    # while cntr < 4: # i used this to test the code
        url = content[cntr][:-1]
        print url
        title = "my title"

        cntr += 1

        response = create_evernote_note_from_url(title,url.encode('utf-8'))
        # print "the response was : ",response
        if "id" in response:
            print "Line number ", cntr, " the response containss a  ", type(response)
            print "the response was : ",response
            print "the url was imported"
            print "+++++"

        else:
            print "something went wrong"
            print "programm stuck at nr - ", cntr

            print "link ", url.encode('utf-8')," will be checked"

            if checkUrl(url.encode('utf-8')):
                print "link ", url.encode('utf-8')," exists"
                print "the programm will be  stopped for a check, has Evernote crashed again?"
                quit()

            else:
                print "link ", url.encode('utf-8')," does not exists or connection offline"
                print "Let us try  the next one"
                print " "

        print "--"


if __name__ == '__main__':
    # change the source file
    source = "list_with_html.txt"
    startline = 0
    html_list_into_evernote(source,startline)
