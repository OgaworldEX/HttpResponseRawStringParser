class HttpRequestRawStringParser:

    delimiter = '\r\n'
    responseRawString = ''
    responseLine = ''

    def __init__(self, responseRawString,delimiter='\r\n'):
        self.responseRawString = responseRawString
        self.delimiter = delimiter

    def getResponseLine(self):
        f = self.responseRawString.find(self.delimiter)
        self.responseLine = self.responseRawString[0:f]
        return self.responseLine

    def getResponseHttpVersion(self):
        index = self.responseLine.find(' ')
        return self.responseLine[0:index]

    def getResponseStatusCode(self):
        findex = self.responseLine.find(' ')
        bindex = self.responseLine.rfind(' ')
        return self.responseLine[findex+1:bindex]

    def getResponseMessage(self):
        index = self.responseLine.rfind(' ')
        return self.responseLine[index+1:len(self.responseLine)]

    def getHeadderString(self):
        index = self.responseRawString.find(self.delimiter + self.delimiter)
        headderStartindex = self.responseRawString[0:index].find(self.delimiter)
        return self.responseRawString[headderStartindex+1:index]

    def getHeadderArray(self):
        index = self.responseRawString.find(self.delimiter + self.delimiter)
        headders = self.responseRawString[0:index].split(self.delimiter)
        del headders[0]
        return headders

    def getHeadderDic(self):
        headders = self.getHeadderArray()
        ret = {}
        for headder in headders:
            tmp = headder.split(': ')
            if len(tmp) > 1:
                ret[tmp[0]] = tmp[1]
        return ret

    def getResponseBodyString(self):
        index = self.responseRawString.rfind(self.delimiter + self.delimiter)
        return self.responseRawString[index + 2:len(self.responseRawString)]


if __name__ == "__main__":

    testString = """HTTP/1.1 200 OK
Content-Type: text/html
X-Content-Type-Options: nosniff
Date: Mon, 20 Jun 19XX 05:19:31 GMT
Server: HTTP server (eggs)
Content-Length: 6141
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Alternate-Protocol: 443:quic
Set-Cookie: sessionid=fjaeiwjfianwfheuaihfvd; Path=/; Max-Age=1000; Expires=Wed, 21-Sep-3000
Connection: close

<html>body</html>"""
    hrsp = HttpRequestRawStringParser(testString ,'\n')
    print('-Result-')
    print('getResponseLine(): ' + hrsp.getResponseLine())
    print('getResponseHttpVersion(): ' + hrsp.getResponseHttpVersion())
    print('getResponseStatusCode(): ' + hrsp.getResponseStatusCode())
    print('getResponseMessage(): ' + hrsp.getResponseMessage())
    print('-')
    print('getHeadderString(): ' + str(hrsp.getHeadderString()))
    print('getHeadderArray(): ' + str(hrsp.getHeadderArray()))
    print('getHeadderDic(): ' + str(hrsp.getHeadderDic()))
    print('-')
    print('getResponseBodyString(): ' + str(hrsp.getResponseBodyString()))

