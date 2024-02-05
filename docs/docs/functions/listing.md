# Danh sách niêm yết

## Công ty niêm yết
```python
listing_companies(live=True)
```

---

- Kết quả trả về như sau cho chế độ realtime, nguồn Wifeed:

```shell
>>> listing_companies(True)
     ticker                                       organName  organTypeCode comGroupCode
0       A32                                         CTCP 32              1        UPCOM
1       AAA                          CTCP Nhựa An Phát Xanh              1         HOSE
2       AAM                            CTCP Thủy sản MeKong              1         HOSE
3       AAS                    CTCP Chứng khoán SmartInvest              4        UPCOM
4       AAT                CTCP Tập Đoàn Tiên Sơn Thanh Hóa              1         HOSE
...     ...                                             ...            ...          ...
1579    XPH                            CTCP Xà phòng Hà Nội              1        UPCOM
1580    YBC              CTCP Xi măng và Khoáng sản Yên Bái              1        UPCOM
1581    YBM             CTCP Khoáng sản Công nghiệp Yên Bái              1         HOSE
1582    YEG                             CTCP Tập đoàn Yeah1              1         HOSE
1583    YTC  CTCP Xuất nhập khẩu Y tế Thành phố Hồ Chí Minh              1        UPCOM
```

- Kết quả trả về cho chế độ realtime, nguồn SSI:

```shell
>>> listing_companies(True, source='SSI')
       organCode ticker  ...                                          organName                  organShortName
0     0104498100    VVS  ...     Công ty Cổ phần Đầu tư Phát triển Máy Việt Nam  Đầu tư Phát triển Máy Việt Nam
1     0109204756    HIO  ...                       Công ty Cổ Phần Helio Energy                    Helio Energy
2     0304941312    XDC  ...       Công ty Cổ phần Xây dựng Công trình Tân Cảng    Xây dựng Công trình Tân Cảng
3     0700519785    THM  ...                      Công ty Cổ phần Tứ Hải Hà Nam                   Tứ Hải Hà Nam
4          10659    HSV  ...              Công ty Cổ phần Tập đoàn HSV Việt Nam                Gang Thép Hà Nội
...          ...    ...  ...                                                ...                             ...
1599  XUANMINHHP    XMP  ...                Công ty Cổ phần Thủy điện Xuân Minh             Thủy điện Xuân Minh
1600         YBC    YBC  ...      Công ty Cổ phần Xi măng và Khoáng sản Yên Bái   Xi măng và Khoáng sản Yên Bái
1601        YBMC    YBM  ...     Công ty Cổ phần Khoáng sản Công nghiệp Yên Bái           Khoáng sản CN Yên Bái
1602     YEGCORP    YEG  ...                     Công ty Cổ phần Tập đoàn Yeah1                  Tập đoàn Yeah1
1603       YTECO    YTC  ...  Công ty Cổ phần Xuất nhập khẩu Y tế Thành phố ...                 XNK Y tế TP.HCM

[1604 rows x 8 columns]

```

- Kết quả trả về cho chế độ offline:

```shell
>>> listing_companies()
  ticker comGroupCode                                          organName   organShortName  ...   VNIT  VNMAT VNREAL  VNUTI
0    SSI         HOSE                    Công ty Cổ phần Chứng khoán SSI  Chứng khoán SSI  ...  False  False  False  False
1    BCM         HOSE  Tổng Công ty Đầu tư và Phát triển Công nghiệp ...      Becamex IDC  ...  False  False   True  False
2    VHM         HOSE                           Công ty Cổ phần Vinhomes         Vinhomes  ...  False  False   True  False

[3 rows x 35 columns]
```

## Các mã chỉ số

```python
indices_listing (lang='vi')
```

```shell
>>> indices_listing (lang='vi')
   comGroupCode parentComGroupCode  comGroupOrder
0       VNINDEX            VNINDEX              1
1      HNXIndex           HNXIndex              2
2          VN30            VNINDEX              2
3        VNCOND            VNINDEX              2
4         HNX30           HNXIndex              3
5    UpcomIndex         UpcomIndex              3
6         VN100            VNINDEX              3
7        VNCONS            VNINDEX              3
8         VNENE            VNINDEX              4
9         VNX50            VNINDEX              4
10        VNFIN            VNINDEX              5
11       VNHEAL            VNINDEX              6
12       VNXALL            VNINDEX              6
13        VNIND            VNINDEX              7
14         VNIT            VNINDEX              8
15        VNMAT            VNINDEX              9
16        VNSML            VNINDEX              9
17        VNMID            VNINDEX             10
18       VNREAL            VNINDEX             10
19        VNALL            VNINDEX             11
20        VNUTI            VNINDEX             11
21    VNDIAMOND            VNINDEX             12
22    VNFINLEAD            VNINDEX             13
23  VNFINSELECT            VNINDEX             14
24         VNSI            VNINDEX             17
```