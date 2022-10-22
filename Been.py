impor os
sistem impor
 waktu impor
cy = ' \033 [92m'
cyy = ' \033 [96m'
lg = ' \033 [92m'
w = ' \033 [97m'
lr = ' \033 [91m'
yl = ' \033 [93m'
t = ' \033 [95m'
x = ' \033 [0m'
os. sistem ("hapus")
cetak ""
cetak ""
print ( cyy + "Subscribe Dulu chanel Rafly Pake i! *" )
os. sistem ("tidur 5" )
os. sistem ("hapus")

cetak ( h + "" "
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~ PEMBUAT SCRIPT DEFACE ~~
~~ PENULIS: MastaBeen ~~
- DIBUAT: 27 JANUARI 2005 ~~
~~ WHATSAPP : +1 (406) 637-6843 ~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"" ")
os. sistem ("tidur 2")
cetak ( cyy + " " )
title = raw_input("Masukkan judul:" )
nick = raw_input ( "Diretas oleh:" )
tim = raw_input("Nama tim:" )
img = raw_input("Tautan gambar:" )
mencetak
print ( cyy + "~~ Di bawah ini pesan halaman awal ya ~~" )
pesan = raw_input("Pesan 1" )
pesan2 = raw_input("Pesan 2" )
pesan3 = raw_input( "Pesan 3" )
pesan4 = raw_input( "Pesan 4" )
mencetak
print ( cyy + "~~ Yang ini pesan untuk adminnya ~~" )
kata = raw_input ( "Kata 1:" )
kata2 = raw_input ( "Kata 2:" )
kata3 = raw_input ( "Kata 3:" )
salam = raw_input ( "Terima kasih kepada:" )
mencetak
print ( cyy + "~~ Nama file (contoh: index.html) ~~" )
namafile = raw_input("Nama file:" )
m1 = "" "<! DOCTYPE html>
<html>
<kepala>
    <judul> "" "
m2 = judul
m3 = "" "</title>
    <meta charset = "UTF-8">
    <meta name = "Penulis" konten = "Seorang Tersakiti <3" />
    <meta name = "copyright" content = "Penjelajah <3" />
    <meta name = "description" content = "Situs web Dimiliki oleh Penjelajah" />
    <link href = 'http: //fonts.googleapis.com/css? family = Islandia: 400.700' rel = 'stylesheet' type = 'text / css'>
    <link href = 'http: //fonts.googleapis.com/css? family = Islandia: 400.700' rel = 'stylesheet' type = 'text / css'>
    <meta property = "og: image" content = "">
        <tipe gaya = "teks / css">
            tubuh {
                meluap: terlihat;
                background-image: url ('https://s22.postimg.org/lq5lty0gx/yh8t9em_VAe_Vw3kh1.jpg');
                warna latar: #000000;
                background-repeat: tidak-ulangi;
                ukuran latar belakang: 100%;
                posisi latar belakang: tengah atas;
                margin: 0 piksel;
                kursor: tidak ada;
                font-family: Islandia, sans-serif;
            }
            Sebuah{
                teks-dekorasi: tidak ada;
            }
            h1 {
            font-family: Islandia, sans-serif;
            ukuran font: 90px;
            warna: #ff;
            margin: 0px 0px 0px;
            }
            h2 {
            font-family: Islandia, sans-serif;
            ukuran font: 40px;
            warna: #000;
            margin: 0 piksel;
            text-shadow: 0 0 3px #fff;
            
            }
            p {
            warna: #000;
            ukuran font: 25px;
            margin: 0 piksel;
            text-shadow: 0 0 3px #fff;
            }
            .fot {
            font-family: Islandia, sans-serif;
            ukuran font: 14px;
            warna: #ff;
            margin: 0 piksel;
            text-shadow: 0 0 3px #000, 0px 0px 5px #000;
            }
             h1 {
            warna: #000;
            text-shadow: 0 0 5px #fff;
        }
        .salam {
    font-family: Arial, sans-serif;
    garis-tinggi: 24px;
    ukuran font: 11px;
    lebar: 50%;
    latar belakang: # 000;
    opasitas: 0,9;
    text-transform: huruf besar;
    indeks-z: 9999;
    batas-radius: 10px;
    -moz-box-shadow: 1px 0px 2px # 000;
    -webkit-box-shadow: 1px 0px 2px # 000;
    kotak-bayangan: 1px 0px 2px # 000;
}
        </ gaya>
    </head>
    <div id = "I301_html">
<jenis skrip = "teks / javascript" src = "http://code.jquery.com/jquery.min.js"> </script>
<script type = "text / javascript"> setTimeout("$('# loading'). fadeOut (5000);", 10000); </skrip>
<style type = "text / css"> # loading {posisi: tetap; atas: 0; kiri: 0; padding-atas: 0px; warna latar: #000; lebar: 100%; tinggi: 100%; warna: hitam; indeks-z: 9000; overflow: tersembunyi;} </style>
<div id = "memuat">
<body onload = "document.fpfocus ()" topmargin = "0" leftmargin = "0" bgcolor = "# 000000" marginheight = "0" marginwidth = "0">
<batas tabel = "0" cellpadding = "2" cellpacing = "0" lebar = "100%">
<tbody> <tr>
</tr>
<tr>
</tr>
</tbody> </table>
<font id = "ResponseData" color = "# ff99cc">
<pre> <jenis skrip = "teks / javascript">
TypingText = fungsi (elemen, interval, kursor, finishCallback) {
  if ((typeof document.getElementById == "undefined") || (typeof element.innerHTML == "undefined")) {
    this.running = benar; // Jangan pernah lari.
    kembali;
  }
  this.elemen = elemen;
  this.finishedCallback = (finishedCallback? finishCallback: function() {return;});
  this.interval = (jenis interval == "tidak terdefinisi"? 100: interval);
  this.origText = this.element.innerHTML;
  this.unparsedOrigText = this.origText;
  this.cursor = (kursor? kursor: "");
  this.currentText = "";
  this.currentChar = 0;
  this.element.typingText = ini;
  if (this.element.id == "") this.element.id = "typingtext" + TypingText.currentIndex ++;
  TypingText.all.push (ini);
  this.running = salah;
  this.inTag = salah;
  this.tagBuffer = "";
  this.inHTMLEntity = salah;
  this.HTMLEntityBuffer = "";
}
TypingText.all = Array baru ();
TypingText.currentIndex = 0;
TypingText.runAll = fungsi () {
  untuk (var i = 0; i <TypingText.all.length; i++) TypingText.all [i] .run();
}
TypingText.prototype.run = fungsi () {
  jika (this.running) kembali;
  if (ketik this.origText == "undefined") {
    setTimeout("document.getElementById ('" + this.element.id + "') .typingText.run ()", this.interval); // Kami belum selesai memuat semua. Bersabarlah.
    kembali;
  }
  if (this.currentText == "") this.element.innerHTML = "";
// this.origText = this.origText.replace (/ <([^ <]) *> /, ""); // Strip HTML dari teks.
  if (this.currentChar <this.origText.length) {
    if (this.origText.charAt (this.currentChar) == "<" &&! this.inTag) {
      this.tagBuffer = "<";
      this.inTag = benar;
      this.currentChar++;
      ini.run();
      kembali;
    } lain jika (this.origText.charAt (this.currentChar) == ">" && this.inTag) {
      this.tagBuffer + = ">";
      this.inTag = salah;
      this.currentText + = this.tagBuffer;
      this.currentChar++;
      ini.run();
      kembali;
    } lain jika (this.inTag) {
      this.tagBuffer + = this.origText.charAt (this.currentChar);
      this.currentChar++;
      ini.run();
      kembali;
    } lain jika (this.origText.charAt (this.currentChar) == "&" &&! this.inHTMLEntity) {
      this.HTMLEntityBuffer = "&";
      this.inHTMLEntity = benar;
      this.currentChar++;
      ini.run();
      kembali;
      } lain jika (this.origText.charAt (this.currentChar) == ";" && this.inHTMLEntity) {
      this.HTMLEntityBuffer + = ";";
      this.inHTMLEntity = salah;
      this.currentText + = this.HTMLEntityBuffer;
      this.currentChar++;
      ini.run();
      kembali;
    } lain jika (this.inHTMLEntity) {
      this.HTMLEntityBuffer + = this.origText.charAt (this.currentChar);
      this.currentChar++;
      ini.run();
      kembali;
    } lain {
      this.currentText + = this.origText.charAt (this.currentChar);
    }
    this.element.innerHTML = this.currentText;
    this.element.innerHTML + = (this.currentChar <this.origText.length - 1? (ketik this.cursor == "function"? this.cursor (this.currentText): this.cursor): "");
    this.currentChar++;
    setTimeout("document.getElementById ('" + this.element.id + "') .typingText.run ()", this.interval);
  } lain {
    this.currentText = "";
    this.currentChar = 0;
        this.running = salah;
        this.finishedCallback();
  }
}
</skrip>
<skrip>
fungsi nonaktifkan pilih (e) {return false}
fungsi mengaktifkan kembali () {mengembalikan benar}
// jika IE4 +
document.onselectstart = Fungsi baru ("return false")
// jika NS6
if (window.sidebar) {
document.onmousedown = nonaktifkan pilih
document.onclick = aktifkan kembali
}
</skrip>
<skrip>
var pesan = "";
fungsi clickIE()
{jika (dokumen.semua)
{(pesan); kembali salah;}}
fungsi clickNS (e) {
jika
(document.layers || (document.getElementById &&! document.all))
{
if (mis.yang == 2 || e.yang == 3) {(pesan); kembali salah;}}}
jika (document.layers)
{document.captureEvents (Acara.MOUSEDOWN); dokumen. onmousedown = klikNS;}
lain
{document.onmouseup = clickNS; document.oncontextmenu = clickIE;}
document.oncontextmenu = Fungsi baru ("return false")
</skrip>
<table style = "background-repeat: no-repeat;" align = "kanan" perbatasan = "0" lebar = "100%">
situs
<tbody> <tr>
<td valign = "top"> <p id = "hack">
<br />
situs
<font color = "Hijau"> <b> ""
m4 = pesan
m5 = "" "<br> <br>
<font color = "Hijau"> <b> ""
m6 = pesan2
m7 = "" "<br> <br>
<font color = "Hijau"> <b> ""
m8 = pesan3
m9 = "" "<br> <br>
<font color = "Hijau"> <b> ""
m10 = pesan4
m11 = "" "</font>
</p> </tr>
</tbody> </table> </div>
situs
<jenis skrip="teks/javascript">
TypingText baru (document.getElementById ("hack"), 50, function (i) {var ar = new Array ("_", ""); return "" + ar [i.length% ar.length];}) ;
TypingText.runAll();
</skrip>
<gaya>
      td
      {
        warna latar: #000000;
        font-family: Kurir Baru;
        ukuran font: 20px;
        warna: #000000;
        batas warna: #000000;
        lebar-perbatasan: 1pt;
        gaya tepi: padat;
        border-collapse: runtuh;
        bantalan: 0pt 3pt;
        vertikal-align: atas;
      }
      meja
      {
        warna tepi: #88aace;
        lebar-perbatasan: 0pt 1pt;
        gaya perbatasan: tanda hubung;
      }
      A: Tautan, A: Dikunjungi
      {
        warna: #88aace;
      }
      A.no:Link, A.no:Kunjungi
      {
warna: #88aace;
        teks-dekorasi: tidak ada;
      }
      A: Arahkan, A: Dikunjungi: Arahkan, A.no: Arahkan, A.no: Dikunjungi: Arahkan kursor
      {
      warna: #88aace;
        warna latar: #2e2e2e;
        teks-dekorasi:
        garis bawahi garis bawah;
      }
      .style1
      {
        warna: #88aace
      }
      .style2
      {
        warna: 1f1f1f
      }
      tubuh
      {
        warna putih;
         
        posisi latar belakang: kanan;
        lampiran-latar belakang: perbaiki;
        </div>
      }
    </ gaya>
        
</div>
</div>
<body oncontextmenu = "return false" onkeydown = "return false">
<tengah>
<h2 kelas = "bersinar"> ""
m12 = waktu
m13 = "" "</h2>
<img src = "" "
t1 = img
t2 = "" "lebar =" 250 "tinggi =" 250 ">
<h2 kelas = "cahaya2">. :: Diretas Oleh ::. <br> <span style = "color: # 000; font-family: Islandia; text-shadow: SkyBlue 0px 0px 10px"> ./ </span > <span style = "color: # 000; font-family: Islandia ; text-shadow: merah 0px 0px 10px"> "" "
t3 = nick
t4 = "" "</span> </b> </h2>
<p> <b> <warna font = "biru"> "
t5 = kata
t6 = "" ". </font> <span style =" font-family: Islandia; warna merah; text-shadow: # 000 0px 0px 3px ">" ""
t7 = kata2
t8 = "" ". </span> <font color=" biru ">" ""
tt = kata3
t9 = "" "</font> <font color=" warna: merah; teks-bayangan: # 000 0px
0px 3px "> </font> <br> # * # * # * #
            </p>
        </span>
            <div style = "ukuran font: 10px; warna: emas; bayangan teks: abu-abu 0px 0px 3px">
        <span style = "font-family: Islandia; font-weight: bold; color: #ffffff"> <p> ~ "" "
t10 = waktu
t11 = "" "~ </p> </span>
    </div>
<div kelas = "salam">
<tabel align = batas tengah = "0">
<tr>
<td lebar = 100% id = CROOTZ>
<perilaku tenda = "gulir" arah = "kiri" scrollamount = "4" scrolldelay = "55" lebar = "100%">
<font size = "5px" style = "font-family: Islandia, sans-serif; warna: hitam; teks-bayangan: 0 0 3px merah, 0px 0px 5px merah">
<b> - = | "" "
T12 = salam
t13 = "" "= - </font>
</marquee>
</td>
</tabel> </div>
<div class="fot">
DUNIA HACKER INDONESIA [+] ANONIM INDONESIA [+] "" "
l1 = waktu
l2 = "" "</div>
</center>
</tubuh>
<object data = "http://flash-mp3-player.net/medias/player_mp3.swf" width = "0" height = "0" type = "application / x-shockwave-flash"> <param value = " #ffffff "name =" bgcolor "> <param value =" mp3 = http: //zizka.free.fr/_muisc/04-kanye_west-amazing_ft._young_jeezy- (HHKingz.net) .mp3 & loop = 1 & autoplay = 1 & volume = 125 " name = "FlashVars"> </object>
</tubuh>
</html> "" "
file = terbuka ( namafile , "w")
file . tulis ( m1 )
file . tulis ( m2 )
file . tulis ( m3 )
file . tulis ( m4 )
file . tulis ( m5 )
file . tulis ( m6 )
file . tulis ( m7 )
file . tulis ( m8 )
file . tulis ( m9 )
file . tulis ( m10 )
file . tulis ( m11 )
file . tulis ( m12 )
file . tulis ( m13 )
file . tulis ( t1 )
file . tulis ( t2 )
file . tulis ( t3 )
file . tulis ( t4 )
file . tulis ( t5 )
file . tulis ( t6 )
file . tulis ( t7)
file . tulis ( t8)
file . tulis (tt)
file . tulis ( t9)
file . tulis ( t10 )
file . tulis ( t11 )
file . tulis ( t12 )
file . tulis ( t13 )
file . tulis ( l1 )
file . tulis ( l2 )
os. sistem ("hapus")
mencetak
cetak "~~ SCRIPT BERHASIL DIBUAT ~~"
print "~~ INI SCRIPT ANDA BERNAMA", namafile
cetak "~~ TERIMA KASIH SUDAH MEMAKAI TOOL SAYA ~~"
mencetak
cetak "BYE...BYE..."

file . tutup ()