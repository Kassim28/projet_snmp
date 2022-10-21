#
# PySNMP MIB module IANAifType-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/IANAifType-MIB.txt
# Produced by pysmi-0.3.4 at Fri Oct 21 16:14:16 2022
# On host NMS platform Linux version 3.10.0-1160.76.1.el7.x86_64 by user root
# Using Python version 3.6.8 (default, Nov 16 2020, 16:55:22) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, Integer32, NotificationType, Gauge32, MibIdentifier, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ObjectIdentity, Bits, mib_2, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Integer32", "NotificationType", "Gauge32", "MibIdentifier", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ObjectIdentity", "Bits", "mib-2", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaifType = ModuleIdentity((1, 3, 6, 1, 2, 1, 30))
ianaifType.setRevisions(('2012-05-17 00:00', '2012-01-11 00:00', '2011-12-18 00:00', '2011-10-26 00:00', '2011-09-07 00:00', '2011-07-22 00:00', '2011-06-03 00:00', '2010-09-21 00:00', '2010-07-21 00:00', '2010-02-11 00:00', '2010-02-08 00:00', '2009-05-06 00:00', '2009-02-06 00:00', '2008-10-09 00:00', '2008-08-12 00:00', '2008-07-22 00:00', '2008-06-24 00:00', '2008-05-29 00:00', '2007-09-13 00:00', '2007-05-29 00:00', '2007-03-08 00:00', '2007-01-23 00:00', '2006-10-17 00:00', '2006-09-25 00:00', '2006-08-17 00:00', '2006-08-11 00:00', '2006-07-25 00:00', '2006-06-14 00:00', '2006-03-31 00:00', '2006-03-30 00:00', '2005-12-22 00:00', '2005-10-10 00:00', '2005-09-09 00:00', '2005-05-27 00:00', '2005-03-03 00:00', '2004-11-22 00:00', '2004-06-17 00:00', '2004-05-12 00:00', '2004-05-07 00:00', '2003-08-25 00:00', '2003-08-18 00:00', '2003-08-07 00:00', '2003-03-18 00:00', '2003-01-13 00:00', '2002-10-17 00:00', '2002-07-16 00:00', '2002-07-10 00:00', '2002-06-19 00:00', '2002-01-04 00:00', '2001-12-20 00:00', '2001-11-15 00:00', '2001-11-06 00:00', '2001-11-02 00:00', '2001-10-16 00:00', '2001-09-19 00:00', '2001-05-11 00:00', '2001-01-12 00:00', '2000-12-19 00:00', '2000-12-07 00:00', '2000-12-04 00:00', '2000-10-17 00:00', '2000-10-02 00:00', '2000-09-01 00:00', '2000-08-24 00:00', '2000-08-23 00:00', '2000-08-22 00:00', '2000-04-25 00:00', '2000-03-06 00:00', '1999-10-08 14:30', '1994-01-31 00:00',))
if mibBuilder.loadTexts: ianaifType.setLastUpdated('201205170000Z')
if mibBuilder.loadTexts: ianaifType.setOrganization('IANA')
class IANAifType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255), SingleValueConstraint(256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272))
    namedValues = NamedValues(("other", 1), ("regular1822", 2), ("hdh1822", 3), ("ddnX25", 4), ("rfc877x25", 5), ("ethernetCsmacd", 6), ("iso88023Csmacd", 7), ("iso88024TokenBus", 8), ("iso88025TokenRing", 9), ("iso88026Man", 10), ("starLan", 11), ("proteon10Mbit", 12), ("proteon80Mbit", 13), ("hyperchannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("ds1", 18), ("e1", 19), ("basicISDN", 20), ("primaryISDN", 21), ("propPointToPointSerial", 22), ("ppp", 23), ("softwareLoopback", 24), ("eon", 25), ("ethernet3Mbit", 26), ("nsip", 27), ("slip", 28), ("ultra", 29), ("ds3", 30), ("sip", 31), ("frameRelay", 32), ("rs232", 33), ("para", 34), ("arcnet", 35), ("arcnetPlus", 36), ("atm", 37), ("miox25", 38), ("sonet", 39), ("x25ple", 40), ("iso88022llc", 41), ("localTalk", 42), ("smdsDxi", 43), ("frameRelayService", 44), ("v35", 45), ("hssi", 46), ("hippi", 47), ("modem", 48), ("aal5", 49), ("sonetPath", 50), ("sonetVT", 51), ("smdsIcip", 52), ("propVirtual", 53), ("propMultiplexor", 54), ("ieee80212", 55), ("fibreChannel", 56), ("hippiInterface", 57), ("frameRelayInterconnect", 58), ("aflane8023", 59), ("aflane8025", 60), ("cctEmul", 61), ("fastEther", 62), ("isdn", 63), ("v11", 64), ("v36", 65), ("g703at64k", 66), ("g703at2mb", 67), ("qllc", 68), ("fastEtherFX", 69), ("channel", 70), ("ieee80211", 71), ("ibm370parChan", 72), ("escon", 73), ("dlsw", 74), ("isdns", 75), ("isdnu", 76), ("lapd", 77), ("ipSwitch", 78), ("rsrb", 79), ("atmLogical", 80), ("ds0", 81), ("ds0Bundle", 82), ("bsc", 83), ("async", 84), ("cnr", 85), ("iso88025Dtr", 86), ("eplrs", 87), ("arap", 88), ("propCnls", 89), ("hostPad", 90), ("termPad", 91), ("frameRelayMPI", 92), ("x213", 93), ("adsl", 94), ("radsl", 95), ("sdsl", 96), ("vdsl", 97), ("iso88025CRFPInt", 98), ("myrinet", 99), ("voiceEM", 100), ("voiceFXO", 101), ("voiceFXS", 102), ("voiceEncap", 103), ("voiceOverIp", 104), ("atmDxi", 105), ("atmFuni", 106), ("atmIma", 107), ("pppMultilinkBundle", 108), ("ipOverCdlc", 109), ("ipOverClaw", 110), ("stackToStack", 111), ("virtualIpAddress", 112), ("mpc", 113), ("ipOverAtm", 114), ("iso88025Fiber", 115), ("tdlc", 116), ("gigabitEthernet", 117), ("hdlc", 118), ("lapf", 119), ("v37", 120), ("x25mlp", 121), ("x25huntGroup", 122), ("transpHdlc", 123), ("interleave", 124), ("fast", 125), ("ip", 126), ("docsCableMaclayer", 127), ("docsCableDownstream", 128), ("docsCableUpstream", 129), ("a12MppSwitch", 130), ("tunnel", 131), ("coffee", 132), ("ces", 133), ("atmSubInterface", 134), ("l2vlan", 135), ("l3ipvlan", 136), ("l3ipxvlan", 137), ("digitalPowerline", 138), ("mediaMailOverIp", 139), ("dtm", 140), ("dcn", 141), ("ipForward", 142), ("msdsl", 143), ("ieee1394", 144), ("if-gsn", 145), ("dvbRccMacLayer", 146), ("dvbRccDownstream", 147), ("dvbRccUpstream", 148), ("atmVirtual", 149), ("mplsTunnel", 150), ("srp", 151), ("voiceOverAtm", 152), ("voiceOverFrameRelay", 153), ("idsl", 154), ("compositeLink", 155), ("ss7SigLink", 156), ("propWirelessP2P", 157), ("frForward", 158), ("rfc1483", 159), ("usb", 160), ("ieee8023adLag", 161), ("bgppolicyaccounting", 162), ("frf16MfrBundle", 163), ("h323Gatekeeper", 164), ("h323Proxy", 165), ("mpls", 166), ("mfSigLink", 167), ("hdsl2", 168), ("shdsl", 169), ("ds1FDL", 170), ("pos", 171), ("dvbAsiIn", 172), ("dvbAsiOut", 173), ("plc", 174), ("nfas", 175), ("tr008", 176), ("gr303RDT", 177), ("gr303IDT", 178), ("isup", 179), ("propDocsWirelessMaclayer", 180), ("propDocsWirelessDownstream", 181), ("propDocsWirelessUpstream", 182), ("hiperlan2", 183), ("propBWAp2Mp", 184), ("sonetOverheadChannel", 185), ("digitalWrapperOverheadChannel", 186), ("aal2", 187), ("radioMAC", 188), ("atmRadio", 189), ("imt", 190), ("mvl", 191), ("reachDSL", 192), ("frDlciEndPt", 193), ("atmVciEndPt", 194), ("opticalChannel", 195), ("opticalTransport", 196), ("propAtm", 197), ("voiceOverCable", 198), ("infiniband", 199), ("teLink", 200), ("q2931", 201), ("virtualTg", 202), ("sipTg", 203), ("sipSig", 204), ("docsCableUpstreamChannel", 205), ("econet", 206), ("pon155", 207), ("pon622", 208), ("bridge", 209), ("linegroup", 210), ("voiceEMFGD", 211), ("voiceFGDEANA", 212), ("voiceDID", 213), ("mpegTransport", 214), ("sixToFour", 215), ("gtp", 216), ("pdnEtherLoop1", 217), ("pdnEtherLoop2", 218), ("opticalChannelGroup", 219), ("homepna", 220), ("gfp", 221), ("ciscoISLvlan", 222), ("actelisMetaLOOP", 223), ("fcipLink", 224), ("rpr", 225), ("qam", 226), ("lmp", 227), ("cblVectaStar", 228), ("docsCableMCmtsDownstream", 229), ("adsl2", 230), ("macSecControlledIF", 231), ("macSecUncontrolledIF", 232), ("aviciOpticalEther", 233), ("atmbond", 234), ("voiceFGDOS", 235), ("mocaVersion1", 236), ("ieee80216WMAN", 237), ("adsl2plus", 238), ("dvbRcsMacLayer", 239), ("dvbTdm", 240), ("dvbRcsTdma", 241), ("x86Laps", 242), ("wwanPP", 243), ("wwanPP2", 244), ("voiceEBS", 245), ("ifPwType", 246), ("ilan", 247), ("pip", 248), ("aluELP", 249), ("gpon", 250), ("vdsl2", 251), ("capwapDot11Profile", 252), ("capwapDot11Bss", 253), ("capwapWtpVirtualRadio", 254), ("bits", 255)) + NamedValues(("docsCableUpstreamRfPort", 256), ("cableDownstreamRfPort", 257), ("vmwareVirtualNic", 258), ("ieee802154", 259), ("otnOdu", 260), ("otnOtu", 261), ("ifVfiType", 262), ("g9981", 263), ("g9982", 264), ("g9983", 265), ("aluEpon", 266), ("aluEponOnu", 267), ("aluEponPhysicalUni", 268), ("aluEponLogicalLink", 269), ("aluGponOnu", 270), ("aluGponPhysicalUni", 271), ("vmwareNicTeam", 272))

class IANAtunnelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("other", 1), ("direct", 2), ("gre", 3), ("minimal", 4), ("l2tp", 5), ("pptp", 6), ("l2f", 7), ("udp", 8), ("atmp", 9), ("msdp", 10), ("sixToFour", 11), ("sixOverFour", 12), ("isatap", 13), ("teredo", 14), ("ipHttps", 15))

mibBuilder.exportSymbols("IANAifType-MIB", PYSNMP_MODULE_ID=ianaifType, IANAifType=IANAifType, IANAtunnelType=IANAtunnelType, ianaifType=ianaifType)