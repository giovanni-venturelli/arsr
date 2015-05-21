<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:n="http://www.ARSR.it">
<xsl:output method="html" version="1.0" encoding="UTF-8" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" indent="yes" />
<xsl:template match="/">
	
	<html xmlsn="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
			<meta name="language" content="italian it" />
			<meta name="author" content="Y-Tech" />
			<title>Administrator - ARSR</title>
			<link rel="stylesheet" type="text/css" media="only screen and (max-device-width: 640px)" href="../css/mobilestyle.css" />
			<link rel="stylesheet" type="text/css" media="(max-width: 766px)" href="../css/smallwinstyle.css" />
			<link rel="stylesheet" type="text/css" media="(min-width: 767px) and (min-device-width: 1024px)"  href="../css/generalstyle.css" />
			<link rel="icon" type="image/png" href="img/favicon2.ico" />
			<title>Attrezzature - ARSR Service</title>
		</head>
		<body>
			<div id="main">
				<xsl:copy-of select="document('../data/header.xml')/*" />
				<div id="subheader">
					<div id="position">
						Ti trovi in: <span lang="en">administrator</span>
                        	<a href="index.xml" id="logout"><span lang="en">LOGOUT</span></a>
					</div>
					<div class="social" id="facebook">
						<a haref="https://www.facebook.com/arsrservice?fref=ts" target="new" title="Pagina Facebook" id="range-logo">pagina <span lang="en">facebook</span>
						</a>
					</div>
				</div>
				<div id="menu">
					<ul>
						<xsl:for-each select="document('../data/administrator.xml')/menu/page">
							<xsl:choose>
								<xsl:when test="not(@id='home')">
									<li class="menulist">
										<a>
											<xsl:attribute name="href"><xsl:value-of select="indirizzo" /></xsl:attribute>
											<xsl:value-of select="name"/>
										</a>
									</li>
								</xsl:when>
								<xsl:otherwise>
									<li class="menulist" id="active">
										<xsl:value-of select="name"/>
									</li>
								</xsl:otherwise>
							</xsl:choose>
						</xsl:for-each>
					</ul>
				</div>
				<div id="content">
					<div id="frase1">benvenuti nella pagina di amministrazione</div>
					<div id="frase2">selezionare l'attività da svolgere dal menù a sinistra</div>
				</div>
				<div id="footer">
					©2014 Y-Tech Giovanni Venturelli, Francesco Agostini, Matteo Gnoato, Nicolò Scapin
				</div>
			</div>
		</body>
	</html>
</xsl:template>
</xsl:stylesheet>
