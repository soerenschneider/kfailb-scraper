from unittest import TestCase

from kfailb import InfoPageParser


class TestInfoPageParser(TestCase):
    def test_parse_data_empty(self):
        parser = InfoPageParser()
        ret = parser.parse_data("   ")
        assert len(ret) == 0


    def test_bla(self):
        x = """<div id="breadcrumbs">
    <ol itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="breadcrumb">
        <li itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/" title="Startseite" itemprop="url"><span itemprop="title">Startseite</span></a></li><li itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/fahrtinfo/" title="Fahrtinfo" itemprop="url"><span itemprop="title">Fahrtinfo</span></a></li><li itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="active"><span itemprop="title">Betriebslage</span></li></ol>
</div>      <h1>Aktuelle Störungen</h1>
    </div>
        
    <div class="container">
        </div>
<div class="container section">
	<div class="row">
		<div class="col-sm-12">
			<h2>
	Störungen bei Bus und Bahn</h2>
<div class="modul">
<table class="table table-striped">
        <tr>
            <td>
                <ul class="info-list"><li style="margin-right:5px;"><span class="number red-text">1</span></li></ul> Streckensanierung zwischen (H) Refrath und (H) Bensberg * Die Bahnen fahren bis 12.08. ca. 03:00h nur zwischen (H) Weiden West und (H) Refrath * Zwischen (H) Refrath und (H) Bensberg sind Ersatzbusse der Linie 101 für Sie eingesetzt *
            </td>
        </tr>
        <tr>
            <td>
                <ul class="info-list"><li style="margin-right:5px;"><span class="number red-text">4</span></li></ul> Folgende Fahrt entfällt * (H) Bocklemünd 12:46h - (H) Äußere Kanalstr. 12:51h - (H) Venloer Str. 12:53h - (H) Friesenplatz 12:58h - (H) Neumarkt 13:02h - (H) BF Deutz/LANXESS arena 13:09h - (H) Stegerwaldsiedlung 13:13h - (H) Wiener Platz 13:18h - (H) Berliner Str. 13:22h - (H) Leuchterstr. 13:28h - (H) Schlebusch 13:33h *
            </td>
        </tr>
        <tr>
            <td>
                <ul class="info-list"><li style="margin-right:5px;"><span class="number red-text">4</span></li></ul> Folgende Fahrt entfällt * (H) Schlebusch 12:54h - (H) Leuchterstr. 12:58h - (H) Berliner Str. 13:03h - (H) Wiener Platz 13:08h - (H) Stegerwaldsiedlung 13:12h - (H) BF Deutz/LANXESS arena 13:16h - (H) Neumarkt 13:24h - (H) Friesenplatz 13:29h - (H) Venloer Str. 13:34h - (H) Äußere Kanalstr. 13:37h - (H) Bocklemünd 13:42h *
            </td>
        </tr>
        <tr>
            <td>
                <ul class="info-list"><li style="margin-right:5px;"><span class="number red-text">7</span></li></ul> Baumaßnahme im Bereich Frechen * Die Bahnen fahren bis 26.08. ca. 03:00h nicht den üblichen Linienweg * Die Bahnen fahren nur zwischen (H) Zündorf und (H) Frechen Bf . * Nutzen Sie bitte die Ersatzbusse der Linie 107 zwischen (H) Frechen Bf. und (H) Frechen Benzelrath *
            </td>
        </tr>
        <tr>
            <td>
                <ul class="info-list"><li style="margin-right:5px;"><span class="number red-text">13</span></li></ul> Folgende Fahrt entfällt * (H) Sülzgürtel 12:52h - (H) Zülpicher Str. 12:55h - (H) Dürener Str. 12:58h - (H) Aachener Str. 13:01h - (H) Venloer Str. 13:05h - (H) Neusser Str. 13:14h - (H) Amsterdamer Str. 13:16h - (H) Wiener Platz 13:21h - (H) Vischeringstr. 13:27h *
            </td>
        </tr>
        <tr>
            <td>
                <ul class="info-list"><li style="margin-right:5px;"><span class="number red-text">16</span></li></ul> Baumaßnahme im Bereich der (H) Heussallee / Museumsmeile * Linie 16 fährt bis 15.08. ca. 03:30h nur zwischen (H) Niehl Sebastianstr. und (H) Heussallee / Museumsmeile * Linie 63 verkehrt zwischen (H) Stadthalle und (H) Hochkreuz * Zwischen (H) Heussallee / Museumsmeile und (H) Hochkreuz sind Ersatzbusse für Sie eingesetzt *
            </td>
        </tr>
        <tr>
            <td>
                <ul class="info-list"><li style="margin-right:5px;"><span class="number red-text">106</span></li><li style="margin-right:5px;"><span class="number red-text">132</span></li></ul> Arbeiten der RheinEnergie im Bereich Im Ferkulum * Die Busse fahren bis 15.08. ca. 04:00h in Richtung (H) Marienburg Südpark bzw. Meschenich nicht den üblichen Linienweg * Die (H) Rosenstr. ist verlegt auf die Severinstr. vor Haus Nr. 97 * Die (H) Severinskirche ist verlegt auf die Severinstr. vor Haus Nr. 33 und die (H) Chlodwigplatz ist verlegt auf die Severinstr. vor Haus Nr. 3-9 *
            </td>
        </tr>
        <tr>
            <td>
                <ul class="info-list"><li style="margin-right:5px;"><span class="number red-text">146</span></li></ul> Fahrbahnsanierung im Bereich der Gleueler Str. * Die Busse fahren bis 08.09. ca. 03:00h nicht den üblichen Linienweg * Die (H) Gleueler Str. ist verlegt auf den Lindenthalgürtel vor Haus Nr. 44 *
            </td>
        </tr>
        <tr>
            <td>
                <ul class="info-list"><li style="margin-right:5px;"><span class="number red-text">159</span></li></ul> Baumaßnahme (H) Steinmetzstr. * Die (H) Steinmetzstr. ist bis 29.11 ca. 03:00h auf die Lilienthalstr. vor die Kreuzung Lilienthalstr/Buchforststr. verlegt *
            </td>
        </tr>
        <tr>
            <td>
                <ul class="info-list"><li style="margin-right:5px;"><span class="number red-text">160</span></li></ul> Wasserrohrbruch im Bereich der (H) Nibelungenstraße * Die Haltestelle Nibelungenstraße wird auf den Linder Mauspfad an die Haltestelle der Linien 162 und 167 in Richtung Porz verlegt * Die Haltestelle Linder Weg wird ersatzlos aufgehoben *
            </td>
        </tr></table></div><h2>
	Störungen der Aufzüge</h2>
<div class="modul">
<b>Folgende Aufzüge sind derzeit außer Betrieb:</b><br /><br /><div class="red-text"><b>Severinstr.</b>, Fahrtrichtung Deutz</div><div class="red-text"><b>Poststr.</b>, Fahrtrichtung Neumarkt</div><div class="red-text"><b>Poststr.</b>, Fahrtrichtung Suevenstr. und Barbarossaplatz</div><div class="red-text"><b>Neumarkt</b>, Fahrtrichtung Poststr.</div><div class="red-text"><b>Mülheim Wiener Platz</b>, Mittelbahnsteig/Ausgang Richtung Linie 4</div><div class="red-text"><b>Bensberg</b>, Mittelbahnsteig</div><br />(Stand: 09.08.2019)

</div>		</div>
	</div>
    </div>"""
        parser = InfoPageParser()
        ret = parser.parse_data(x)
        print(ret)