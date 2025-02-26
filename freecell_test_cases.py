from dataclasses import dataclass


# data class for test case, has values and suits
# values represents the values of the cards. Each row is a columnn in the game.
# This is the fastest way to enter the game board.
# suits is similarly each row for each column in the game.
@dataclass
class TestCase:
    values: str
    suits: str


test_cases = [
    TestCase(
        values="""
9 6 4 1 5 4 13
11 11 11 7 6 1 4
1 8 1 2 13 13 7
13 10 9 8 11 12 3
10 4 2 5 3 6
3 12 5 12 12 7
9 5 7 6 3 10
2 8 8 10 2 9
""",
        suits="""
DSDHCHH
HCSSDCS
DDSHCDH
SSSHDDH
CCSDSH
CCSSHD
HHCCDD
CCSHDC
""",
    ),
    TestCase(
        values="""
7 12 9 2 12 8 12
4 1 7 10 9 9 8
1 5 11 1 10 10 6
6 3 5 7 13 1 13
3 3 11 11 4 2
6 13 5 12 2 8
4 7 5 10 8 13
9 11 4 6 2 3
""",
        suits="""
CCSHHHD
HDHHDHC
CDDSCSC
HHSSSHD
CSSCSC
SCHSSS
CDCDDH
CHDDDD
""",
    ),
    TestCase(
        values="""
1 9 2 12 5 6 6
1 6 1 12 11 5 5
10 13 9 9 11 9 13
4 2 4 6 7 4 13
8 8 8 3 11 3
2 8 10 7 7 10
7 11 3 13 3 2
12 1 4 5 12 10
""",
        suits="""
HDCHSHD
SCDSDHC
CHCHSSC
SDHSHCD
DCSCHS
SHSSDD
CCHSDH
CCDDDH
""",
    ),
    TestCase(
        values="""
8 1 6 12 3 5 5
3 2 9 8 5 11 12
6 5 4 11 4 10 1
6 2 6 3 7 2 10
9 9 2 12 12 4
11 9 4 10 13 1
1 8 13 10 13 7
3 8 11 13 7 7
""",
        suits="""
DCSSHDC
CDHCHHH
DSDCCHS
CCHSCSD
SCHDCH
DDSCSD
HHHSCD
DSSDSH
""",
    ),
    TestCase(
        values="""
10 2 2 9 6 4 8
11 1 7 3 12 7 1
2 13 4 12 5 3 8
1 7 8 5 5 6 7
6 13 3 10 1 6
12 12 9 5 3 11
9 2 8 13 11 10
4 4 11 10 13 9
""",
        suits="""
HSCCHDS
DHSHCHS
HSCSSSD
CCCCHSD
CHDDDD
HDSDCC
HDHCHC
SHSSDD
""",
    ),
    TestCase(
        values="""
11 10 8 3 12 6 3
7 1 2 9 7 10 5
13 9 3 11 5 1 8
12 4 7 3 1 5 4
6 4 6 8 12 7
5 13 10 11 13 13
9 1 6 10 9 4
8 2 2 11 2 12
""",
        suits="""
SHDHSCD
SCSCCDS
HDCHDHH
HSHSDCH
HCDSCD
HCSDDS
SSSCHD
CHDCCD
""",
    ),
    TestCase(
        values="""
1 11 8 4 7 8 3
5 11 3 11 6 8 9
3 13 4 12 4 8 7
5 9 4 2 10 13 5
3 1 1 11 9 2
6 12 2 13 5 10
7 7 2 12 12 13
9 6 1 6 10 10
""",
        suits="""
CDCSCSH
SCCHHDC
SCDCHHD
CHCSHHH
DDHSSH
CHDDDD
HSCSDS
DSSDCS
""",
    ),
    TestCase(
        values="""
3 7 5 8 2 7 11
13 8 4 1 13 2 5
10 3 2 5 10 11 11
1 4 12 9 6 11 5
3 10 4 7 9 1
6 3 6 1 9 12
8 13 13 8 6 4
12 2 9 10 12 7
""",
        suits="""
HSDDHDC
HHDSDCC
HSDSCSH
CSDHSDH
CSHCCH
DDHDSC
CCSSCC
SSDDHH
""",
    ),
    TestCase(
        values="""
2 4 8 13 10 6 6
12 11 1 1 11 3 10
9 9 13 2 2 5 11
5 10 9 8 4 5 6
7 7 9 12 4 5
4 6 3 10 7 12
12 8 8 1 7 3
1 11 3 13 13 2
""",
        suits="""
HDSHSDH
DDSCSDH
DCSCDSC
DDHCSHS
DSSCCC
HCSCCH
SHDDHH
HHCDCS
""",
    ),
    TestCase(
        values="""
3 5 10 12 6 13 4
7 1 6 1 5 5 8
4 8 10 9 7 1 4
9 2 9 3 2 1 4
13 13 11 12 8 7
10 11 11 8 13 12
10 5 3 6 9 3
6 12 7 2 2 11
""",
        suits="""
HHHHCCC
DHDCCSC
DDDCSDH
SDHDCSS
HDSDHH
SHCSSS
CDCHDS
SCCSHD
""",
    ),
    TestCase(
        values="""
6 13 4 7 10 9 11
13 5 1 8 3 10 11
11 12 5 3 11 7 13
1 8 4 7 2 10 5
12 5 4 2 6 9
9 2 8 3 10 12
6 2 3 12 8 4
7 1 6 9 1 13
""",
        suits="""
HDCDDCS
HSSCDHH
DHHCCCS
HHHHHSC
SDDSDD
SDDSCC
CCHDSS
SCSHDC
""",
    ),
    TestCase(
        values="""
13 1 4 13 6 1 9
2 3 11 11 4 12 3
6 13 1 6 6 10 9
7 8 7 3 9 8 8
10 2 5 4 4 5
3 7 10 8 11 12
12 10 12 2 5 11
1 2 9 7 5 13
""",
        suits="""
CSDHHCD
DDSCSSS
CSDSDDS
CDDHCHC
CHHHCS
CSHSDD
HSCCDH
HSHHCD
""",
    ),
    TestCase(
        values="""
7 8 9 10 11 12 13
7 8 9 10 11 12 13
7 8 9 10 11 12 13
7 8 9 10 11 12 13
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
""",
        suits="""
DDDDDDD
CCCCCCC
SSSSSSS
HHHHHHH
DDDDDD
CCCCCC
SSSSSS
HHHHHH
""",
    ),
    TestCase(
        values="""
5 1 3 5 7 4 6
8 10 13 5 13 8 4
2 6 2 12 11 9 6
5 8 11 10 2 12 7
11 8 9 13 9 10
13 3 10 12 6 7
4 7 2 11 1 3
1 12 9 4 3 1
""",
        suits="""
CHDDHSS
CCCHHDH
SHHHCCD
SHDHDDS
HSDSSS
DHDCCD
CCCSDS
CSHDCS
""",
    ),
    TestCase(
        values="""
7 4 10 12 9 1 2
7 13 11 1 6 8 8
10 3 9 7 11 13 8
9 12 6 5 5 12 2
8 11 11 2 10 4
7 2 13 9 3 5
5 4 3 10 4 6
1 12 3 13 6 1
""",
        suits="""
HHDDDCH
DSHSDCH
CCSCSCS
HHCHCSC
DCDSHD
SDHCHS
DCSSSS
DCDDHH
""",
    ),
    TestCase(
        values="""
2 13 1 4 10 10 13
4 13 6 11 4 5 2
8 8 5 9 5 9 8
6 11 12 1 12 3 12
3 9 8 1 3 7
11 6 12 4 10 9
7 3 1 10 7 2
11 6 7 5 13 2
""",
        suits="""
SCHHHCD
SSHSDDD
SHSCHDD
SDCDSCH
HSCSSD
CDDCDH
HDCSCH
HCSCHC
""",
    ),
    TestCase(
        values="""
8 13 11 12 9 1 10
12 12 5 5 6 6 3
4 8 13 8 1 6 9
2 3 10 13 8 11 1
4 2 6 13 2 7
9 4 5 11 10 5
2 7 4 11 3 9
12 1 3 10 7 7
""",
        suits="""
HCDDSHS
SHSCSCD
CCDSDDD
DSHHDSS
SHHSCC
CHHCDD
SDDHCH
CCHCSH
""",
    ),
    TestCase(
        values="""
7 13 6 11 12 4 3
5 9 11 13 1 12 12
1 4 1 13 4 2 9
3 8 10 9 12 11 1
2 3 8 11 8 9
5 10 3 4 13 7
6 6 7 2 10 10
8 5 5 6 2 7
""",
        suits="""
CHDSSSH
HHCCCHD
DHSSCDS
DSCDCDH
CSHHDC
DDCDDS
SCHSHS
CCSHHD
""",
    ),
    TestCase(
        values="""
10 1 4 2 9 10 3
13 1 8 3 9 1 8
9 3 4 11 3 5 2
13 8 11 6 12 10 10
12 6 7 6 5 7
12 8 2 13 1 4
12 9 5 7 5 11
7 2 4 11 13 6
""",
        suits="""
CSSHCSC
DCHDHHD
DSHCHHC
SSHSCDH
HCSHCH
DCSCDC
SSSDDS
CDDDHD
""",
    ),
    TestCase(
        values="""
6 13 10 5 5 8 4
1 13 11 4 4 8 5
7 2 13 6 8 3 12
2 8 1 2 11 4 11
9 9 1 9 12 7
1 9 6 13 3 2
3 5 7 10 10 11
7 10 6 12 3 12
""",
        suits="""
DHHSCHS
CCCDCCH
DDDSDCC
SSDHDHS
SHHCHS
SDCSHC
SDHSDH
CCHSDD
""",
    ),
    TestCase(
        values="""
4 4 2 8 1 3 5
1 1 13 11 7 5 12
9 2 9 2 5 10 4
8 2 7 1 5 13 3
3 7 12 6 8 10
9 11 11 12 11 6
6 10 8 3 13 6
9 12 10 4 13 7
""",
        suits="""
DCHDSSC
CDDHSHH
CCHDDDS
HSHHSHC
HDCHSH
SCSDDC
SSCDCD
DSCHSC
""",
    ),
    TestCase(
        values="""
9 5 10 1 2 11 7
2 1 12 9 7 8 6
7 10 3 13 6 1 12
7 4 11 4 4 12 13
5 3 3 8 6 11
13 6 5 12 2 11
13 8 3 9 5 10
8 1 2 10 9 4
""",
        suits="""
HSCSDCC
HDCCHSS
SHCSHHH
DSSCDDD
CHSCDH
HCDSCD
CHDDHS
DCSDSH
""",
    ),
    TestCase(
        values="""
13 10 7 8 12 10 13
4 1 8 12 5 2 2
10 9 12 6 6 7 9
9 12 5 11 4 9 6
3 7 10 5 5 4
7 1 1 11 3 11
2 13 6 1 8 3
11 13 4 8 2 3
""",
        suits="""
CCCCHDH
CSSSCHS
SDCDHHH
SDHHSCS
SSHSDD
DDCSDD
DDCHHC
CSHDCH
""",
    ),
    TestCase(
        values="""
2 6 3 11 13 3 1
13 11 7 6 12 13 4
4 9 8 7 3 10 12
4 5 9 10 6 7 8
9 12 8 1 4 11
3 9 1 2 2 8
10 11 7 12 10 2
5 1 5 13 5 6
""",
        suits="""
HDDHDHS
CCDCDHC
DHCSCHC
SCCCSHD
SSSCHD
SDDCSH
SSCHDD
DHHSSH
""",
    ),
    TestCase(
        values="""
4 5 10 4 7 7 10
4 11 8 9 12 3 11
11 4 3 1 11 2 9
10 2 13 6 1 3 8
6 8 1 9 9 13
13 5 7 2 7 2
12 1 6 8 6 10
5 12 3 13 12 5
""",
        suits="""
HHCDHDS
CCSDDCH
SSHDDDH
DCCSHDC
HHSSCD
HSSSCH
SCCDDH
CCSSHD
""",
    ),
    TestCase(
        values="""
8 12 9 6 2 4 12
3 10 1 10 5 7 8
1 6 11 9 7 12 6
1 13 4 7 13 12 7
10 2 5 9 2 5
6 8 2 11 4 3
5 13 11 13 10 11
8 9 1 3 4 3
""",
        suits="""
SDCDHSH
SHHDHCH
CHHHHCC
SDCDSSS
SDSDCC
SDSSDH
DCDHCC
CSDCHD
""",
    ),
    TestCase(
        values="""
7 5 4 3 5 11 8
1 3 1 3 7 8 8
9 9 10 10 9 13 7
1 1 6 2 4 12 4
6 13 13 7 12 5
2 6 2 8 12 4
10 6 12 11 13 11
9 5 10 3 11 2
""",
        suits="""
HCCHSHD
HDDCCCH
CDHDHHD
CSHDDDH
CCSSHD
SDHSCS
CSSSDC
SHSSDC
""",
    ),
    TestCase(
        values="""
9 11 13 8 11 4 13
7 12 2 5 5 12 7
4 3 3 6 3 5 1
6 9 2 10 13 1 4
8 9 9 2 1 3
11 7 8 11 12 2
10 7 10 4 5 6
8 10 1 6 12 13
""",
        suits="""
DCCCHHS
HDSCHSS
DDHHSSS
CCHHHDC
SSHDHC
DDHSCC
DCCSDD
DSCSHD
""",
    ),
    TestCase(
        values="""
3 10 7 4 4 12 9
12 11 4 6 1 9 10
3 8 7 12 11 3 8
13 7 13 5 2 6 2
4 5 13 9 8 1
2 10 8 10 5 12
9 1 13 6 6 1
11 7 11 2 5 3
""",
        suits="""
HSSHDDC
CHSDDDC
CSCHSSD
HHSCHCS
CDCHHC
DHCDHS
SSDHSH
CDDCSD
""",
    ),
    TestCase(
        values="""
2 11 10 6 9 10 9
11 5 13 7 3 7 3
6 2 8 4 13 9 1
13 12 2 10 1 3 7
5 12 1 11 1 12
5 13 8 10 4 12
7 6 3 8 4 4
9 2 11 6 5 8
""",
        suits="""
CHDHHHC
CHSCHDS
DSCSDDS
HDHCCCS
CCHDDS
DCHSDH
HSDSCH
SDSCSD
""",
    ),
    TestCase(
        values="""
8 6 5 6 4 13 12
11 11 1 3 1 10 3
3 1 11 1 4 7 2
12 13 12 2 12 10 4
11 8 7 10 9 8
2 13 7 10 6 13
5 2 5 6 9 8
4 7 9 9 5 3
""",
        suits="""
CHCSSDH
CDSDCHS
CHSDDCS
SCCCDCC
HSHSSD
HHDDDS
SDDCHH
HSCDHH
""",
    ),
    TestCase(
        values="""
10 2 9 8 7 5 11
8 7 3 11 9 13 13
1 12 12 10 7 6 8
11 9 2 5 1 9 5
12 1 4 10 10 11
4 3 7 3 13 12
6 1 3 6 4 13
2 5 4 8 6 2
""",
        suits="""
DSDCCCH
DDHDHHD
HDHCSDS
CCCSDSD
CCSSHS
DCHDCS
HSSSHS
HHCHCD
""",
    ),
    TestCase(
        values="""
3 5 5 3 12 2 8
3 7 3 10 10 4 5
1 2 5 8 1 11 6
13 12 7 9 9 7 8
11 6 2 13 4 9
8 11 12 2 1 13
4 1 6 12 4 9
11 10 6 10 13 7
""",
        suits="""
CSHDCHH
HSSHDHD
HDCSDHH
CSCCSHC
SCSHCD
DDDCSD
DCSHSH
CSDCSD
""",
    ),
    TestCase(
        values="""
9 8 3 5 3 9 1
11 5 11 10 13 11 8
1 4 7 13 10 2 11
10 6 13 3 2 6 12
7 6 12 8 4 9
10 5 4 2 7 1
3 1 9 12 13 8
6 7 5 12 2 4
""",
        suits="""
DSSHHHH
SDCSCHD
CHHHDSD
CCSCHHH
DDCHDC
HCSDSD
DSSDDC
SCSSCC
""",
    ),
    TestCase(
        values="""
13 4 13 9 10 4 11
12 11 1 7 2 8 5
10 1 3 7 3 12 3
11 5 4 13 6 6 7
2 11 8 10 2 9
8 5 13 8 12 12
5 10 1 1 6 9
7 6 4 2 9 3
""",
        suits="""
SCDCSSH
HSDDDHD
HHSSHDC
DCDHHCH
HCDDSS
SSCCCS
HCSCSH
CDHCDD
""",
    ),
    TestCase(
        values="""
1 6 8 13 5 4 13
4 8 6 1 10 12 7
4 3 11 7 9 12 2
3 7 9 6 1 2 12
5 10 13 4 5 8
2 11 8 11 2 10
12 6 10 1 13 3
3 5 7 9 9 11
""",
        suits="""
HHCHDSD
HSCSHSH
DHSDSDD
CSCSCCH
CSCCSH
SHDDHC
CDDDSS
DHCDHC
""",
    ),
    TestCase(
        values="""
11 8 2 11 12 10 2
4 5 9 11 6 9 1
4 8 7 5 9 3 8
4 5 13 1 5 3 3
8 2 10 7 4 9
10 13 2 10 6 13
6 1 12 1 6 11
7 12 7 3 13 12
""",
        suits="""
DSDHCCS
CHHCSSH
SDDCDSC
DSHSDDC
HHSHHC
HCCDCD
DDHCHS
SSCHSD
""",
    ),
    TestCase(
        values="""
7 10 6 10 3 4 9
11 12 12 2 7 1 5
4 6 12 8 5 9 6
1 2 8 3 2 10 6
3 1 5 9 11 7
13 9 11 1 11 4
12 13 2 8 13 8
5 10 4 13 3 7
""",
        suits="""
CCSDHSH
HDCHDSD
CDHHSSC
CCCCSHH
SDHDSH
SCCHDH
SDDDCS
CSDHDS
""",
    ),
    TestCase(
        values="""
13 2 10 8 11 6 10
11 10 8 7 2 5 5
12 5 8 1 7 9 6
1 4 4 13 1 8 7
13 10 6 4 12 9
6 4 3 9 7 3
13 3 11 12 11 3
2 2 5 12 9 1
""",
        suits="""
DSCDCDS
DDSSDSC
SDCDHCS
SCDHCHC
SHCHHD
HSDSDH
CSHDSC
HCHCHH
""",
    ),
    TestCase(
        values="""
10 11 6 4 1 10 13
6 5 1 9 4 9 11
1 3 7 12 11 6 5
8 13 4 5 9 8 2
6 8 12 13 2 10
3 7 3 5 7 8
2 12 3 2 1 10
13 12 7 4 11 9
""",
        suits="""
CSHHHHS
CHDSCHH
CCDDCSC
HHSDDDH
DSSCSD
SCHSSC
CHDDSS
DCHDDC
""",
    ),
    TestCase(
        values="""
1 8 1 4 5 12 11
7 7 6 4 8 5 8
13 10 12 7 10 3 9
4 8 11 5 6 3 5
13 2 2 6 10 13
7 3 11 11 6 12
4 2 13 9 9 1
12 9 3 2 1 10
""",
        suits="""
CSDCDCD
HSSHDCC
SDHCHHD
SHCSHDH
HSCDCC
DSSHCD
DDDHCS
SSCHHS
""",
    ),
    TestCase(
        values="""
2 7 9 10 9 1 3
2 10 5 13 1 2 9
8 13 6 4 8 8 4
5 9 7 11 11 12 1
11 6 1 7 5 2
12 10 10 11 12 8
7 3 3 3 13 13
12 6 4 4 6 5
""",
        suits="""
SCSSCHC
CHDSDDD
SHCCHDD
CHSDCCC
HSSHSH
DDCSHC
DSDHDC
SDHSHH
""",
    ),
    TestCase(
        values="""
11 12 2 10 5 8 8
9 3 9 12 6 1 2
6 2 12 7 8 3 10
9 4 13 6 3 4 2
10 1 7 5 4 9
12 11 3 13 13 1
11 8 7 5 11 13
1 4 10 7 6 5
""",
        suits="""
CHDDDSC
HHCDCDC
SHSDDDS
DHCDCCS
CHHSSS
CDSDSC
HHCHSH
SDHSHC
""",
    ),
    TestCase(
        values="""
13 9 3 13 6 1 11
7 2 12 3 10 6 12
3 8 5 9 13 7 12
4 7 4 8 7 1 2
5 10 2 1 10 8
11 13 6 3 11 5
11 6 4 10 9 8
1 4 2 5 12 9
""",
        suits="""
SCHCCSD
DCSDSDC
SHDDDSH
CHSDCHD
CCSCHC
HHSCSH
CHDDHS
DHHSDS
""",
    ),
    TestCase(
        values="""
13 11 3 8 7 13 12
2 12 10 5 1 3 11
5 6 6 9 2 1 3
8 4 13 9 12 8 7
6 7 4 13 2 11
10 4 9 10 5 1
7 5 1 8 10 6
9 4 12 2 11 3
""",
        suits="""
DDHCCSS
CCCDSSH
HDHDDHD
SCHSDDD
CHDCSS
DHCHSC
SCDHSS
HSHHCC
""",
    ),
    TestCase(
        values="""
9 9 12 2 3 1 13
8 7 11 11 10 13 1
6 8 12 10 3 10 6
2 3 8 10 5 1 8
2 9 3 12 4 13
11 5 13 9 7 1
5 7 4 12 11 4
2 6 6 4 5 7
""",
        suits="""
DSSSHCC
DSDCCHS
DHCSSDS
HCSHDHC
CHDDHS
HSDCCD
HHCHSS
DHCDCD
""",
    ),
    TestCase(
        values="""
2 5 3 1 10 1 10
8 12 3 4 5 2 9
6 8 7 1 11 11 5
11 12 9 12 1 5 2
6 3 8 13 4 10
2 11 3 7 4 9
12 13 13 7 9 7
13 6 8 4 6 10
""",
        suits="""
CDHSCHS
CHCHSHC
DSHCSDC
CSHCDHS
SDDSCH
DHSCDS
DHDDDS
CCHSHD
""",
    ),
    TestCase(
        values="""
5 2 2 11 6 8 8
12 8 4 4 2 11 9
7 1 8 12 11 13 3
10 10 5 11 10 1 4
5 2 6 1 3 9
13 10 4 13 3 7
12 3 13 7 12 6
6 5 7 9 1 9
""",
        suits="""
SHSSCCH
HDDHDCH
CHSDHHC
HDCDSSC
HCHDSD
DCSSDS
CHCHSS
DDDSCC
""",
    ),
    TestCase(
        values="""
11 6 13 13 10 9 9
7 7 3 12 4 9 5
6 5 11 4 12 5 7
8 8 3 12 2 10 2
6 10 8 8 7 3
1 4 2 11 10 6
9 1 12 4 1 13
11 2 5 1 3 13
""",
        suits="""
SHSHCDH
DCHDDSD
CSDCHHS
HCSSCHD
DSDSHC
CHSCDS
CHCSSD
HHCDDC
""",
    ),
    TestCase(
        values="""
9 6 9 2 6 1 12
9 12 3 8 8 3 13
4 2 11 5 5 6 4
13 9 4 3 4 6 2
7 2 11 8 3 10
5 11 1 10 7 7
11 10 8 10 1 5
12 13 13 7 1 12
""",
        suits="""
HSCCCSS
DDDSHCD
DSSCHDC
CSSHHHD
DHHCSC
DCDDSH
DHDSCS
HHSCHC
""",
    ),
    TestCase(
        values="""
10 10 12 12 5 2 6
13 5 9 9 3 3 11
13 9 5 8 13 11 11
11 3 2 1 8 7 9
7 6 4 12 2 6
4 6 2 10 8 12
4 4 1 7 10 13
5 8 7 3 1 1
""",
        suits="""
DHHCSHH
DDSHHSS
HCCDSHD
CCSCSSD
DDCSDS
SCCSCD
HDDCCC
HHHDSH
""",
    ),
    TestCase(
        values="""
6 11 5 2 3 11 1
2 6 13 3 4 1 5
2 5 12 2 11 1 7
8 9 4 5 11 8 10
13 6 7 13 3 9
6 12 12 3 10 13
7 8 10 4 4 8
10 7 9 12 9 1
""",
        suits="""
DDSHHSD
DSDSDCH
SDDCHHS
HCSCCSH
SHCCDD
CSHCCH
DDDCHC
SHSCHS
""",
    ),
    TestCase(
        values="""
9 2 6 13 10 6 1
12 11 2 11 1 12 7
6 2 5 9 8 9 7
4 7 3 10 4 5 1
2 5 3 13 12 9
13 8 3 11 12 10
6 5 4 10 8 8
1 7 4 3 13 11
""",
        suits="""
DCSSSDC
HDSSDCD
HDCCSHS
HHDCCDS
HHHHDS
DDCHSD
CSDHHC
HCSSCC
""",
    ),
    TestCase(
        values="""
5 6 1 10 5 9 1
2 8 3 7 8 5 4
4 3 10 3 11 13 13
7 6 5 9 8 7 3
7 1 13 9 10 2
2 4 11 11 8 12
12 13 10 12 2 4
6 9 12 11 1 6
""",
        suits="""
CSDSDHC
HHHCCSD
CDDSHHC
SCHDDDC
HSDSCS
DSDSSH
SSHCCH
HCDCHD
""",
    ),
    TestCase(
        values="""
4 7 4 8 13 3 9
8 8 9 13 1 10 3
7 7 10 11 2 6 1
12 5 8 12 2 6 11
13 9 6 1 7 9
2 1 12 10 10 3
2 6 4 12 5 5
5 11 11 3 4 13
""",
        suits="""
HHDDCSC
SHHDCDC
SCHDCDH
SSCCDHH
HDCDDS
HSHSCH
SSSDCD
HSCDCS
""",
    ),
    TestCase(
        values="""
9 2 1 2 1 4 6
2 5 7 1 12 3 11
9 13 5 12 4 11 7
12 10 6 13 4 11 4
7 9 5 10 6 8
10 5 2 3 6 8
3 3 8 9 1 10
7 13 13 11 8 12
""",
        suits="""
SCDDSHC
HSHCDSC
CCDHDDC
CCSSCHS
DDCDHH
SHSDDS
HCDHHH
SDHSCS
""",
    ),
    TestCase(
        values="""
2 1 6 9 5 4 12
7 1 9 5 10 11 3
12 2 3 8 8 9 11
2 5 13 10 11 4 4
3 13 13 2 4 9
3 1 8 6 10 1
5 6 8 7 7 10
12 6 7 12 11 13
""",
        suits="""
CHHSDCC
HSHCCCS
DHDHDCH
DHSSDSH
HHCSDD
CCSDDD
SSCDCH
SCSHSD
""",
    ),
    TestCase(
        values="""
3 5 5 7 9 8 6
8 8 2 12 10 7 4
9 1 10 2 11 11 6
9 6 3 1 12 13 5
4 13 8 11 3 1
13 3 10 7 5 12
7 12 1 13 10 2
9 2 4 11 6 4
""",
        suits="""
CDSSHDD
SCSSDCS
CDCHCDH
DCHHDCC
HDHHDC
SSSDHC
HHSHHD
SCCSSD
""",
    ),
    TestCase(
        values="""
4 13 9 8 3 1 12
5 2 9 2 11 7 9
5 13 8 6 10 7 3
1 11 6 7 4 2 9
13 3 10 12 3 10
10 1 12 1 4 11
6 4 11 8 12 5
2 7 8 13 6 5
""",
        suits="""
CHCHCDD
CHHCSHS
DDCHDCS
CDSSSSD
SHHHDS
CSCHDH
DHCDSH
DDSCCS
""",
    ),
    TestCase(
        values="""
7 13 11 2 8 12 12
8 7 10 10 3 11 4
6 9 3 4 1 1 2
11 8 9 9 6 12 3
6 3 7 13 5 13
5 12 8 1 13 9
2 10 6 4 7 2
1 11 5 10 4 5
""",
        suits="""
SHDHSSD
HHSDCSD
HSSSDHC
CDDHSHD
CHDCCS
SCCCDC
DHDHCS
SHDCCH
""",
    ),
    TestCase(
        values="""
2 4 7 7 10 6 4
12 4 13 1 3 10 9
5 13 10 9 3 13 6
5 6 7 10 3 7 1
1 4 11 8 5 11
2 8 9 13 12 12
5 8 6 3 9 2
2 8 12 1 11 11
""",
        suits="""
CDCDSHH
SSHDCCC
HCDDSSC
CDHHHSC
SCCHDS
HDHDDC
SCSDSD
SSHHDH
""",
    ),
    TestCase(
        values="""
4 1 5 7 2 10 13
12 13 9 9 10 4 12
6 11 8 13 3 4 1
2 11 13 2 6 5 4
9 6 12 12 10 11
2 8 8 10 7 3
3 7 7 8 3 5
6 9 11 5 1 1
""",
        suits="""
SSDCCHS
HDDCSDD
DCCHDHD
DHCSSSC
SHSCCS
HHDDSH
SDHSCH
CHDCHC
""",
    ),
    TestCase(
        values="""
12 1 11 10 9 6 2
8 7 9 13 10 7 2
9 8 3 9 5 10 4
13 6 5 8 1 7 12
6 5 3 11 4 6
4 13 12 11 2 1
2 8 13 3 5 7
4 11 3 10 12 1
""",
        suits="""
SHCSCHC
DHDCDCS
HHHSDCH
SCCSDDD
DHSDCS
SHCHHS
DCDDSS
DSCHHC
""",
    ),
    TestCase(
        values="""
7 12 4 11 3 3 4
7 13 10 12 6 1 9
9 5 3 11 2 9 6
10 8 6 6 12 4 8
13 8 7 2 1 13
11 8 9 12 10 13
5 2 11 7 1 4
3 2 1 5 5 10
""",
        suits="""
HDDSHCS
CHDCSHH
CHDCHDC
SSHDSCC
SDSCDD
DHSHHC
DDHDCH
SSSSCC
""",
    ),
    TestCase(
        values="""
7 8 5 2 3 2 3
8 10 9 1 5 4 6
11 13 6 11 9 12 1
10 1 4 11 6 9 6
4 7 9 12 12 10
8 3 2 12 13 4
3 13 2 10 7 5
1 8 11 13 7 5
""",
        suits="""
DHCSHDS
CCHSHHS
CDHDDDC
HHCSCCD
DCSCHD
SCHSCS
DHCSHD
DDHSSS
""",
    ),
    TestCase(
        values="""
2 2 5 11 4 11 8
7 12 1 10 9 13 1
8 6 7 10 3 1 13
7 13 8 12 6 9 11
6 11 4 10 9 1
3 5 13 8 2 4
12 3 9 6 7 2
5 12 4 10 3 5
""",
        suits="""
SHDHDSS
HSSSSSD
DDSCCHC
DDHDCDD
HCCDCC
HCHCDH
CDHSCC
SHSHSH
""",
    ),
    TestCase(
        values="""
12 8 2 1 9 10 2
4 11 7 5 8 4 9
5 7 10 12 9 12 1
3 4 2 8 12 8 2
6 6 6 3 10 11
7 13 9 1 10 13
3 6 13 5 5 1
13 3 11 11 4 7
""",
        suits="""
HHCHDSH
CHHDSHS
HDDCCSC
CSSCDDD
DHSDCC
CHHDHS
HCDSCS
CSDSDS
""",
    ),
    TestCase(
        values="""
3 7 10 12 4 8 1
10 3 5 3 12 5 9
8 11 7 4 6 7 4
6 12 6 8 4 9 13
2 8 13 9 12 11
11 2 1 13 1 9
2 10 5 6 7 1
10 13 11 3 2 5
""",
        suits="""
DSDDDHD
SHDCSSH
CHDSDHH
CHSDCDS
DSCSCD
SCHDSC
SCHHCC
HHCSHC
""",
    ),
    TestCase(
        values="""
10 6 10 2 13 9 11
7 7 11 9 12 6 11
10 6 3 12 10 4 13
4 5 5 3 2 13 13
11 4 7 1 7 8
5 1 1 12 8 2
2 8 3 3 8 1
12 4 5 9 6 9
""",
        suits="""
SSCDHDD
SDSCDHH
HDDSDHD
DHSHHCS
CSCSHS
DHDCCC
SHCSDC
HCCHCS
""",
    ),
    TestCase(
        values="""
12 1 3 3 4 7 6
12 10 5 8 3 9 1
6 7 2 3 11 5 1
4 12 13 13 8 5 8
11 9 10 9 2 2
7 10 2 13 4 8
4 6 12 5 9 11
6 11 13 7 10 1
""",
        suits="""
SSCSDHH
CDDHDCH
SCDHHSC
CDDHCHS
DDSSSC
SHHSSD
HDHCHC
CSCDCD
""",
    ),
    TestCase(
        values="""
7 11 13 11 13 8 13
2 7 1 8 7 4 5
10 11 5 5 12 13 6
9 8 2 9 4 2 6
7 4 12 3 5 2
4 6 12 12 1 1
6 10 9 10 11 3
9 3 1 8 3 10
""",
        suits="""
SHCCDDS
DHCHCDD
CSSCHHC
CCCSSHD
DHDCHS
CHSCHD
SDHSDS
DHSSDH
""",
    ),
    TestCase(
        values="""
1 4 2 6 13 10 4
6 2 7 10 8 8 13
11 10 11 13 9 3 3
11 3 9 7 5 6 8
1 5 4 12 13 9
1 3 2 1 2 4
6 7 11 8 12 9
7 10 12 5 12 5
""",
        suits="""
SDHCSHC
HSCCDSD
DDSCSDC
CHDHHDH
HDHHHC
CSDDCS
SSHCSH
DSDCCS
""",
    ),
    TestCase(
        values="""
10 11 12 10 6 8 3
7 9 3 7 13 13 10
4 12 1 6 1 2 2
3 6 13 5 5 6 4
12 10 8 5 12 8
7 4 11 9 11 2
11 3 8 9 7 9
4 2 13 1 5 1
""",
        suits="""
HCHDSHC
CSDDHCC
HSSDHHS
SCSSHHC
CSSDDD
SDSCHC
DHCDHH
SDDDCC
""",
    ),
    TestCase(
        values="""
7 5 9 11 1 13 7
10 1 3 6 11 2 9
3 11 10 2 8 13 6
8 4 13 12 6 4 12
4 5 9 7 10 3
4 11 7 6 12 12
5 2 9 2 1 5
10 8 3 8 1 13
""",
        suits="""
CSCHHSS
SSSHSCD
HDHSDHD
CDCDCCH
SDSHCD
HCDSCS
CHHDCH
DHCSDD
""",
    ),
    TestCase(
        values="""
11 10 2 13 8 10 10
6 2 7 5 3 2 6
12 9 13 12 11 5 12
10 8 1 9 4 5 4
5 6 9 7 4 12
7 8 11 13 4 7
3 2 8 1 3 1
11 1 3 6 13 9
""",
        suits="""
HHSHSDS
SHSHCCD
DCCSSCH
CDCHSSH
DHDCCC
HHDDDD
HDCSSH
CDDCSS
""",
    ),
    TestCase(
        values="""
3 2 5 9 7 8 4
7 11 1 8 13 10 10
11 12 7 13 7 5 11
12 1 12 4 6 9 5
9 10 10 1 11 4
3 3 2 4 8 9
6 5 12 6 6 13
8 2 2 1 13 3
""",
        suits="""
HCCDCSC
HHHHCDH
DDDHSSS
CCHSCHD
SCSSCH
CSDDCC
DHSHSD
DHSDSD
""",
    ),
    TestCase(
        values="""
3 5 5 5 6 7 11
8 3 1 5 13 1 9
1 2 13 4 8 10 4
12 6 3 10 12 9 1
3 2 11 2 12 9
9 13 4 4 12 8
2 8 10 6 11 7
13 6 7 11 10 7
""",
        suits="""
HHSDDHC
DCCCDHS
SSCSSDH
HCSSCHD
DCHDDD
CSCDSH
HCCSDS
HHCSHD
""",
    ),
    TestCase(
        values="""
2 11 10 1 10 12 11
2 6 7 2 10 13 9
12 4 8 7 4 5 5
8 8 12 1 3 6 4
3 5 4 10 9 13
11 3 13 1 9 6
11 1 5 7 8 13
6 2 3 7 12 9
""",
        suits="""
SDHSSHH
DSCHDDD
SHDHCDH
SHCDDCD
CCSCSH
CSSCCH
SHSSCC
DCHDDH
""",
    ),
    TestCase(
        values="""
2 9 3 13 11 12 8
4 6 2 5 13 3 4
12 8 11 6 10 4 7
2 9 11 7 13 1 6
10 9 5 12 1 9
8 3 3 7 4 7
12 6 10 10 2 11
13 5 1 1 8 5
""",
        suits="""
SSHHHDH
SSHDCCH
SCSHDDC
DDDSDDC
CHSHSC
SSDDCH
CDHSCC
SHCHDC
""",
    ),
    TestCase(
        values="""
13 4 5 12 8 1 2
2 13 1 5 10 6 5
9 4 8 11 2 1 13
8 6 12 11 11 9 2
11 10 10 3 3 3
13 3 6 7 9 6
9 7 10 12 4 7
1 4 7 5 8 12
""",
        suits="""
DHDSDHH
DSDHSCS
DDSDSSH
CHDHCHC
SDCSHC
CDDDSS
CHHCSS
CCCCHH
""",
    ),
    TestCase(
        values="""
1 9 2 12 5 6 6
1 6 1 12 11 5 5
10 13 9 9 11 9 13
4 2 4 6 7 4 13
8 8 8 3 11 3
2 8 10 7 7 10
7 11 3 13 3 2
12 1 4 5 12 10
""",
        suits="""
HDCHSHD
SCDSDHC
CHCHSSC
SDHSHCD
DCSCHS
SHSSDD
CCHSDH
CCDDDH
""",
    ),
    TestCase(
        values="""
13 5 2 13 3 10 11
6 7 11 3 7 4 12
4 5 2 5 3 8 11
4 8 5 12 9 1 2
12 4 12 7 13 6
10 10 7 1 1 8
9 3 6 11 9 10
9 6 2 13 1 8
""",
        suits="""
SDCCHCD
HDSCCDD
SCSHSSH
CDSSCDD
CHHHDD
HSSSHH
DDCCSD
HSHHCC
""",
    ),
    TestCase(
        values="""
10 6 7 1 2 11 8
10 7 13 9 8 9 11
13 1 5 10 4 12 11
2 1 5 6 5 3 3
2 7 6 12 12 13
2 13 8 1 6 4
4 7 3 10 8 3
9 4 12 5 11 9
""",
        suits="""
HSCSCSC
DHCCSDH
DDCSHCD
SCSDHDS
HSCHDS
DHDHHD
SDHCHC
SCSDCH
""",
    ),
    TestCase(
        values="""
4 3 3 5 11 4 8
5 7 13 6 7 9 6
1 2 10 3 10 6 6
12 12 2 10 4 9 8
2 7 7 5 13 1
11 9 10 11 4 5
8 3 1 8 12 9
13 11 12 13 1 2
""",
        suits="""
HDCHSDH
DDSCCSS
SHDHCHD
SCSSSDC
DSHSHH
CCHDCC
SSDDDH
CHHDCC
""",
    ),
    TestCase(
        values="""
8 10 1 3 4 6 5
12 3 2 6 8 3 9
2 8 13 1 11 9 9
5 7 6 8 11 13 4
7 10 11 9 1 2
2 3 4 6 11 12
12 5 13 1 7 4
13 12 10 10 7 5
""",
        suits="""
CDHHDDH
CCSHDDD
CHDDHSC
DSCSCHH
DCSHSD
HSSSDD
HCCCCC
SSHSHS
""",
    ),
    TestCase(
        values="""
3 7 11 3 4 3 6
2 12 8 1 5 11 8
10 5 6 7 10 2 13
11 12 1 12 7 7 4
5 4 10 12 6 1
11 13 9 2 13 10
8 5 1 4 2 9
8 9 3 9 13 6
""",
        suits="""
HHDDSSH
SDDCSCS
SDCDCDS
HHHSSCH
HDDCDD
SDCCHH
HCSCHH
CDCSCS
""",
    ),
    TestCase(
        values="""
2 10 5 5 9 11 5
1 12 13 1 13 8 9
5 2 11 13 6 6 8
7 12 8 4 7 9 13
3 12 10 3 10 3
3 2 12 10 9 11
2 7 6 4 4 11
7 4 8 1 6 1
""",
        suits="""
HHSDHDC
SSDDCHD
HDHHCHC
DHSCHSS
SCCHSC
DCDDCS
SSSDHC
CSDHDC
""",
    ),
    TestCase(
        values="""
7 12 2 8 4 5 3
5 8 11 9 2 12 9
2 7 4 10 9 1 10
10 2 6 5 4 6 7
9 12 1 3 11 6
3 13 8 4 13 7
11 3 6 1 13 10
13 1 8 5 11 12
""",
        suits="""
SCDDDDH
SCDDCHH
HCSDCDC
HSDHHSD
SSSSHH
DSSCDH
SCCHHS
CCHCCD
""",
    ),
    TestCase(
        values="""
7 2 5 10 13 11 9
12 4 8 7 11 5 10
11 3 8 7 5 3 13
1 10 9 12 6 3 13
4 6 2 8 2 8
7 10 12 11 4 9
5 6 3 1 4 9
1 6 13 1 12 2
""",
        suits="""
CHDDCSD
SHDHDSS
CCHSHDS
CHHDHHH
DSDSSC
DCHHCS
CDSDSC
SCDHCC
""",
    ),
    TestCase(
        values="""
2 7 1 13 7 12 10
12 5 13 12 7 6 9
2 3 7 8 10 9 1
9 5 3 4 11 6 3
9 8 13 2 5 13
4 4 8 6 5 6
11 3 8 11 12 10
11 4 1 10 2 1
""",
        suits="""
SHHHDSH
DDDHSSC
HCCDCDC
HCHHCDS
SHCCHS
DSCHSC
SDSDCS
HCSDDD
""",
    ),
    TestCase(
        values="""
9 6 4 7 11 2 9
3 2 7 3 10 5 10
7 2 3 4 13 8 3
1 5 9 1 8 6 5
11 6 10 12 1 4
9 8 8 12 4 12
2 13 11 13 11 7
10 6 5 1 12 13
""",
        suits="""
DDHSDCS
HSHDCHD
CHSSSCC
SSHHDHD
CCHHCC
CHSDDS
DCSHHD
SSCDCD
""",
    ),
    TestCase(
        values="""
7 12 6 8 11 6 13
5 3 2 2 9 2 9
8 1 4 10 10 5 7
11 3 1 12 8 3 1
8 5 12 10 11 9
1 4 13 3 9 4
13 2 12 7 7 11
6 5 4 10 13 6
""",
        suits="""
DHSDDCC
DCCHDDH
HSDHSCC
HDHSSSD
CSCDSC
CCSHSH
DSDHSC
HHSCHD
""",
    ),
    TestCase(
        values="""
1 3 10 3 4 7 10
9 13 5 3 8 2 1
4 13 4 6 4 6 7
12 2 11 13 8 12 7
11 13 2 9 2 8
9 12 1 12 7 10
11 10 5 11 3 9
8 5 6 5 1 6
""",
        suits="""
SSCDSHH
CHDHCHD
HCCCDDC
DCCSSSD
DDSDDH
SCCHSD
HSSSCH
DHHCHS
""",
    ),
    TestCase(
        values="""
13 12 6 10 5 8 3
5 1 8 8 12 13 10
1 11 2 10 9 4 13
11 5 3 2 6 13 3
9 12 9 7 4 2
9 11 7 1 11 5
6 12 6 4 2 1
7 4 8 3 10 7
""",
        suits="""
SHDHDDS
HDCHCHC
SHCDCHC
CSDDHDH
HSSHCH
DSSHDC
CDSDSC
DSSCSC
""",
    ),
    TestCase(
        values="""
1 12 12 6 1 5 10
5 10 13 11 4 12 1
7 3 4 9 12 7 13
2 8 13 2 11 9 9
3 7 6 8 11 6
3 1 5 7 4 5
10 4 11 8 2 3
9 13 10 6 8 2
""",
        suits="""
SSDDDCC
SHDHHHC
DHCSCHS
CDCSSCH
SCSHCH
CHDSDH
DSDCDD
DHSCSH
""",
    ),
    TestCase(
        values="""
4 13 9 1 5 2 8
6 11 9 3 7 11 4
6 9 11 5 7 1 6
7 3 3 10 12 11 10
4 13 7 8 5 1
5 12 9 2 10 1
2 6 12 8 13 12
10 13 4 2 8 3
""",
        suits="""
HDHCCSS
SCSDHDS
DCHHDSH
SHSHSSC
CHCHSH
DDDDSD
CCCCSH
DCDHDC
""",
    ),
    TestCase(
        values="""
2 10 12 11 7 7 10
3 2 1 13 9 1 4
13 5 6 8 6 10 12
12 11 1 2 4 1 11
2 5 7 3 9 3
5 6 9 8 12 8
4 8 5 7 4 9
10 13 6 3 13 11
""",
        suits="""
HHDDSHS
HCHCSDD
HCHDSDH
CHSSHCC
DHCDCS
SDHCSS
SHDDCD
CSCCDS
""",
    ),
    TestCase(
        values="""
11 12 4 3 10 12 1
7 6 1 6 11 9 1
1 9 4 2 3 9 10
8 9 13 12 11 2 13
5 12 8 7 6 13
2 3 8 2 6 3
10 8 11 10 5 4
7 5 4 7 5 13
""",
        suits="""
HCSDCSS
DDCSCDD
HCHDHHD
DSCDDHS
SHCSCD
CSSSHC
SHSHDC
CCDHHH
""",
    ),
    TestCase(
        values="""
7 5 3 11 13 1 10
8 3 12 5 2 12 3
2 10 5 4 6 13 11
7 9 5 7 6 8 4
10 8 6 8 12 2
13 1 13 7 10 1
9 4 12 9 2 6
3 11 1 11 4 9
""",
        suits="""
HSSHDSD
CCCDCDD
HHHHSCD
SCCDCSS
SDDHHS
SCHCCH
HCSDDH
HSDCDS
""",
    ),
    TestCase(
        values="""
12 2 8 13 8 2 7
1 1 1 4 7 8 3
10 3 4 11 10 13 10
5 6 1 11 9 13 11
6 12 3 9 12 8
9 5 13 7 3 9
5 5 6 4 10 2
7 12 4 11 6 2
""",
        suits="""
CCHSDHH
DCHDCCH
CSSSSDD
DHSCCHD
CSCSDS
HCCDDD
HSDHHD
SHCHSS
""",
    ),
    TestCase(
        values="""
9 1 3 1 11 5 11
3 7 4 10 13 5 2
2 11 6 1 8 12 1
9 8 9 13 7 7 5
12 9 13 12 10 7
4 3 4 6 4 2
5 2 11 6 13 10
12 8 10 3 8 6
""",
        suits="""
DSDDCDH
HDSDSSS
CSDHSHC
CHHCHCC
SSDCHS
CSHCDH
HDDHHC
DCSCDS
""",
    ),
    TestCase(
        values="""
10 6 8 6 9 10 11
5 13 1 7 6 11 12
4 5 12 9 2 8 1
12 4 8 11 12 7 7
3 3 13 2 8 2
1 4 9 5 3 4
5 13 9 3 10 7
2 1 11 13 6 10
""",
        suits="""
HHCCDCC
SSCSDHS
HCDHCDH
CSSDHHC
SDDSHH
SCCDHD
HHSCSD
DDSCSD
""",
    ),
    TestCase(
        values="""
8 1 13 11 13 13 1
7 10 6 9 4 8 5
10 3 4 11 6 6 11
1 12 4 10 4 7 3
13 9 12 12 7 7
8 12 5 8 2 11
2 5 9 3 2 2
10 5 3 6 9 1
""",
        suits="""
CDHSCSC
CSCCHDH
DHDHSHC
HCSCCSC
DHHDHD
SSCHSD
DDSDCH
HSSDDS
""",
    ),
    TestCase(
        values="""
12 6 10 1 1 3 12
7 4 13 10 7 11 10
2 10 5 8 9 2 5
11 9 2 6 3 6 5
3 7 4 13 11 3
6 12 9 4 12 8
8 11 7 1 1 4
2 13 13 5 8 9
""",
        suits="""
SHCCHHC
HDDDCCS
SHSDDDD
HSHDSSC
CDCSSD
CHCHDH
CDSSDS
CHCHSH
""",
    ),
    TestCase(
        values="""
8 3 9 7 2 10 3
7 9 3 6 8 8 5
5 6 1 1 12 11 5
4 10 4 9 13 8 7
6 13 10 6 11 2
9 5 11 1 4 3
4 12 1 2 12 10
7 2 11 13 13 12
""",
        suits="""
CDCDHDC
SSHCDHC
DDSHCDS
DHHHSSH
SHSHSS
DHCDSS
CSCCDC
CDHCDH
""",
    ),
    TestCase(
        values="""
11 4 10 6 2 2 4
12 6 11 13 8 5 3
13 7 4 13 6 1 8
13 3 2 8 12 1 9
8 12 2 4 11 10
5 3 5 12 9 10
7 1 11 9 5 10
7 6 3 7 1 9
""",
        suits="""
SHHDHDC
HCCCHSD
HHDDSDD
SCSCDSD
SCCSDC
CSDSSD
DCHHHS
CHHSHC
""",
    ),
    TestCase(
        values="""
3 7 1 8 4 9 9
6 4 2 2 9 5 5
2 7 9 10 4 1 3
1 2 10 13 11 10 12
3 13 1 8 8 12
10 8 5 11 7 12
6 4 13 7 11 6
11 3 5 13 12 6
""",
        suits="""
DSHHHCS
DDHSDDS
CHHDCSH
DDSHCHD
CDCSDC
CCCSCS
HSSDDS
HSHCHC
""",
    ),
    TestCase(
        values="""
11 12 4 2 1 10 8
7 1 7 3 9 6 9
4 5 6 9 12 6 10
9 6 10 13 12 1 3
12 4 1 8 5 8
7 3 11 13 2 5
11 13 10 13 11 4
2 7 2 8 3 5
""",
        suits="""
CCSCCHS
DHCSHDD
DHCSDSC
CHSCHDC
SHSDSH
SDHDHD
DHDSSC
SHDCHC
""",
    ),
    TestCase(
        values="""
8 9 5 10 13 4 6
5 2 6 1 11 12 6
2 4 1 1 8 10 8
3 5 6 13 7 10 2
11 13 12 11 4 13
7 3 11 7 3 12
9 9 10 2 4 1
3 7 12 9 5 8
""",
        suits="""
CDDCHDS
CSCHSSH
HHSDHHD
DSDSSSD
HDHCSC
CSDDCD
SHDCCC
HHCCHS
""",
    ),
    TestCase(
        values="""
9 7 9 5 8 11 1
9 5 9 2 11 2 1
4 6 8 11 11 5 4
12 10 10 5 2 10 12
6 3 4 1 13 6
10 4 13 8 13 7
7 2 8 1 3 12
7 13 3 6 3 12
""",
        suits="""
SHDSDHC
HCCSDDS
HCHCSDC
DHSHHDH
SSDHHD
CSCCDC
DCSDCS
SSHHDC
""",
    ),
    TestCase(
        values="""
8 10 13 9 7 5 6
10 2 9 1 4 2 1
11 3 7 2 8 6 7
13 6 11 7 5 13 11
1 12 4 3 13 4
10 6 12 12 12 3
1 5 9 3 4 5
11 10 9 2 8 8
""",
        suits="""
CSHDDHH
DSHSHDD
HSSCDDC
CSSHSSC
HHDHDS
HCCDSD
CCSCCD
DCCHHS
""",
    ),
    TestCase(
        values="""
10 7 13 9 3 8 9
12 6 5 6 4 10 8
10 11 3 5 3 13 10
12 4 5 1 2 1 9
4 9 4 2 11 7
7 5 11 13 6 12
6 11 3 1 12 1
13 2 8 7 2 8
""",
        suits="""
SSDSDHH
DHCDCCS
DDSHHSH
HHSSHHD
DCSSHH
CDSCCS
SCCDCC
HCDDDC
""",
    ),
    TestCase(
        values="""
8 11 4 3 12 1 3
1 5 10 4 12 8 2
1 6 8 5 9 10 7
7 9 6 9 11 11 9
13 5 10 7 13 3
6 4 6 12 3 8
2 12 5 1 2 11
13 10 7 2 4 13
""",
        suits="""
CSSCHDD
HCHCCSD
SHDHSDD
SHSCHCD
CSCCDS
DHCDHH
CSDCHD
SSHSDH
""",
    ),
    TestCase(
        values="""
8 9 2 7 7 2 2
12 8 9 4 10 9 5
12 2 13 11 11 4 6
5 9 6 1 4 6 7
12 11 1 3 1 5
8 10 3 10 7 3
5 1 6 3 11 13
13 4 12 13 8 10
""",
        suits="""
CHDHSHC
HDSHHDH
SSSHCCH
CCCCDSC
DDSSHD
SDCSDH
SDDDSD
HSCCHC
""",
    ),
    TestCase(
        values="""
11 13 8 6 12 4 10
3 13 1 2 7 11 4
5 7 7 6 8 4 9
9 3 10 11 5 3 13
2 11 2 9 10 7
12 8 4 2 12 6
1 10 5 13 1 6
9 5 12 8 3 1
""",
        suits="""
CSCSDHH
CDSDHHC
SDCDSSD
SHDDCDC
HSSCSS
HDDCSH
HCHHCC
HDCHSD
""",
    ),
    TestCase(
        values="""
3 2 10 3 10 7 5
8 7 3 5 9 1 5
7 6 6 8 2 13 4
1 1 13 6 11 10 4
13 12 3 12 12 8
1 10 13 4 4 8
9 11 2 5 9 11
2 7 11 6 12 9
""",
        suits="""
DSSSCDH
SSHSHCD
CCSCCHC
DSSDDDD
CSCCDD
HHDSHH
SSHCCC
DHHHHD
""",
    ),
    TestCase(
        values="""
1 8 13 12 10 8 2
6 9 11 12 4 4 11
2 12 9 3 7 10 8
6 9 13 13 5 2 1
3 6 13 4 11 1
1 8 7 6 10 10
2 11 3 7 4 3
9 5 5 12 5 7
""",
        suits="""
DDHSHSS
CCCDHCS
HHHCHSH
SSDSDDS
SHCDHH
CCSDCD
CDHCSD
DSHCCD
""",
    ),
    TestCase(
        values="""
2 2 11 5 8 6 4
10 4 1 8 6 3 10
9 11 10 1 2 6 5
5 3 4 13 4 2 12
3 7 9 12 7 1
11 10 13 13 1 12
7 9 13 5 8 8
6 7 3 12 9 11
""",
        suits="""
DCCHHHS
DCDCSHC
HDSCHCD
CDHSDSH
CHSCCS
HHDCHS
DDHSSD
DSSDCS
""",
    ),
    TestCase(
        values="""
11 11 1 11 13 8 9
8 13 10 5 4 4 1
10 5 9 10 12 3 3
2 6 10 8 2 6 1
13 6 7 12 9 1
12 5 4 6 12 11
5 3 2 7 3 7
13 9 4 8 2 7
""",
        suits="""
HSSDCHD
CSSHCDH
HSSDHSD
HHCSDDC
DCHDHD
SDHSCC
CHCDCS
HCSDSC
""",
    ),
    TestCase(
        values="""
8 9 6 10 4 8 1
1 10 5 12 5 6 4
9 3 13 12 11 7 4
6 9 10 5 1 12 13
10 6 8 7 7 7
8 3 1 12 5 11
2 13 3 2 11 2
13 4 2 9 3 11
""",
        suits="""
DHHDCHH
SHDSCDS
SDCHHCH
CDSHDDD
CSCDSH
SSCCSD
SSHHCD
HDCCCS
""",
    ),
    TestCase(
        values="""
3 2 5 4 6 1 1
4 9 8 8 12 13 3
2 7 4 13 9 9 6
6 13 6 9 5 10 10
11 5 8 3 2 1
7 12 12 2 10 11
12 3 11 1 7 7
11 13 5 8 4 10
""",
        suits="""
CDHHCSH
SSCHSHD
HHCCCHH
SDDDSHD
DCSHSC
SCHCCH
DSCDCD
SSDDDS
""",
    ),
    TestCase(
        values="""
10 8 6 4 3 1 12
11 8 13 10 6 11 1
7 12 5 5 4 10 2
2 8 9 1 7 6 11
11 5 6 5 12 3
1 3 8 7 2 12
4 9 3 13 9 13
7 13 4 2 9 10
""",
        suits="""
DSCDDDC
DHHHSCH
CDDSCSD
SDSCHDH
SCHHSS
SHCDCH
SCCCHD
SSHHDC
""",
    ),
    TestCase(
        values="""
13 5 2 5 10 9 12
9 11 8 2 3 11 6
3 4 13 1 3 11 2
12 7 7 9 10 5 6
6 2 12 8 7 13
11 3 10 1 10 8
5 12 13 1 4 4
9 4 7 6 1 8
""",
        suits="""
DDCSCSS
HHHHHDC
SSCSDSS
HHSDDHS
HDCSCS
CCHHSD
CDHCCH
CDDDDC
""",
    ),
    TestCase(
        values="""
10 8 4 7 4 10 13
1 12 1 2 8 1 7
6 9 3 9 5 12 1
11 5 9 11 3 13 11
6 8 2 5 8 5
4 3 6 9 13 2
10 11 7 4 6 2
12 12 13 3 10 7
""",
        suits="""
DCCHSCC
CHHCSDS
DSSDSSS
DDCSCHC
HHDCDH
DDCHDH
HHCHSS
CDSHSD
""",
    ),
    TestCase(
        values="""
12 7 7 7 2 5 1
1 6 2 11 4 10 10
8 3 3 8 2 1 12
13 4 5 4 13 6 13
13 6 6 4 12 1
10 7 3 11 2 3
9 8 10 12 9 9
11 8 5 11 9 5
""",
        suits="""
DCHDDHD
HSCDHSH
HSHSHCS
HSSCCDS
DCHDHS
DSCHSD
SDCCCH
SCDCDC
""",
    ),
    TestCase(
        values="""
1 6 11 8 2 10 11
12 8 9 5 3 5 12
5 7 5 6 2 7 6
8 13 10 9 7 1 13
4 11 4 12 8 12
3 10 2 1 13 4
1 3 9 3 2 7
9 13 6 4 11 10
""",
        suits="""
CSSHDCH
DCSHCCH
SCDHHHC
SSDHSSD
SCCCDS
DSSDCD
HSCHCD
DHDHDH
""",
    ),
    TestCase(
        values="""
13 11 1 4 2 9 5
1 9 3 8 10 5 1
1 11 2 10 6 6 7
10 11 6 4 3 7 2
4 13 10 8 12 9
8 2 8 3 13 12
9 5 13 6 11 12
7 12 5 4 3 7
""",
        suits="""
CSSHSDH
CCDSCSH
DDHHSCD
DCHCHSD
SHSCSS
DCHSSH
HCDDHC
CDDDCH
""",
    ),
    TestCase(
        values="""
4 11 13 9 8 13 8
1 3 1 7 10 3 2
10 9 4 4 7 11 6
3 10 13 11 2 2 4
13 6 2 11 8 6
7 12 1 6 12 5
1 5 12 3 10 8
12 7 5 5 9 9
""",
        suits="""
DSSSSHD
HCDCCSC
HCSHHDS
DDCHDHC
DCSCCD
DCSHHD
CHDHSH
SSCSDH
""",
    ),
    TestCase(
        values="""
4 11 9 6 11 4 2
9 12 11 8 1 10 9
7 8 6 12 5 2 5
13 3 10 4 3 3 8
13 1 9 2 7 1
1 7 6 5 7 5
2 13 3 12 10 6
13 12 10 11 4 8
""",
        suits="""
SDSSSDC
CSHSCHD
CHDHSHC
CDSCSCC
HSHDDH
DSCDHH
SSHCCH
DDDCHD
""",
    ),
    TestCase(
        values="""
11 3 11 10 8 12 13
9 3 2 13 6 13 9
1 4 1 8 12 7 9
5 8 4 11 5 3 3
2 12 6 4 6 7
7 10 2 13 6 11
4 9 10 7 1 5
8 10 1 2 12 5
""",
        suits="""
DHSCCHS
SDCHDDH
CHSSSSD
DHSCCCS
DDSDCH
DDSCHH
CCSCDS
DHHHCH
""",
    ),
    TestCase(
        values="""
10 10 4 6 2 7 13
5 6 8 1 11 13 6
5 3 3 7 3 8 9
11 12 12 10 7 2 12
6 8 8 2 1 9
4 5 11 5 3 13
4 9 10 2 9 13
12 7 4 1 1 11
""",
        suits="""
DCSSDSC
SCDHDHH
CCHHSCD
CDCSDSS
DHSCDH
DHSDDD
HCHHSS
HCCCSH
""",
    ),
    TestCase(
        values="""
13 5 1 10 1 3 7
4 4 13 9 3 10 11
6 11 5 9 2 9 2
2 10 12 7 12 2 4
6 5 10 8 6 13
7 1 11 13 8 3
4 8 5 8 11 7
12 9 1 6 12 3
""",
        suits="""
DCDSHDD
HSCCHHD
CSHHCDS
HDHSSDC
DDCHSS
CSCHSS
DDSCHH
CSCHDC
""",
    ),
    TestCase(
        values="""
12 12 11 9 9 10 5
1 8 6 1 3 4 11
3 6 12 8 13 11 7
3 13 10 5 10 1 7
6 3 10 2 13 2
9 11 7 1 13 4
8 6 4 2 9 12
5 2 8 4 7 5
""",
        suits="""
DCSHCCC
SSHHCDC
HDHHCDD
SDDSHCH
CDSCHH
SHCDSH
DSCDDS
DSCSSH
""",
    ),
    TestCase(
        values="""
5 4 7 10 11 3 5
11 1 5 12 13 2 9
4 9 7 3 10 6 11
12 4 7 12 7 13 3
8 2 1 9 12 2
11 9 10 10 6 3
1 6 8 1 6 8
13 13 2 5 4 8
""",
        suits="""
DSCCDDS
CHHHDHH
DSSSDDS
CHDSHSC
HDSCDC
HDSHCH
CHCDSD
CHSCCS
""",
    ),
    TestCase(
        values="""
10 11 7 9 7 6 6
5 1 8 2 1 4 4
10 12 13 12 3 5 9
2 11 6 1 3 9 4
5 11 2 8 12 2
13 11 9 12 13 3
8 3 1 10 8 4
5 7 10 6 7 13
""",
        suits="""
HDHCDHC
DHSSDCS
DDHCCCD
CCSCHHD
HSHCHD
SHSSDD
HSSCDH
SSSDCC
""",
    ),
    TestCase(
        values="""
13 11 1 3 6 13 9
9 12 11 2 7 1 3
9 12 8 2 7 4 9
4 3 7 7 5 5 10
13 5 13 3 6 4
10 2 12 11 8 10
4 8 10 6 6 8
2 12 1 5 11 1
""",
        suits="""
DDDHCHD
SDHSSHS
HHCHHCC
HCCDHDD
CSSDHD
CDCSHH
SDSSDS
CSCCCS
""",
    ),
    TestCase(
        values="""
3 10 5 13 7 5 4
6 13 7 2 11 12 1
13 2 10 8 6 7 7
10 5 4 5 12 3 3
1 8 6 11 12 10
8 9 11 2 3 9
1 11 2 6 9 9
12 8 13 4 1 4
""",
        suits="""
SSDHSCD
CSDSDCC
DHCHDCH
HHCSSHD
DCHCHD
DCSCCS
SHDSDH
DSCHHS
""",
    ),
]
