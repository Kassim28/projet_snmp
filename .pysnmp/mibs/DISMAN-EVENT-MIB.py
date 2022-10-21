#
# PySNMP MIB module DISMAN-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/DISMAN-EVENT-MIB.txt
# Produced by pysmi-0.3.4 at Fri Oct 21 18:23:35 2022
# On host NMS platform Linux version 3.10.0-1160.76.1.el7.x86_64 by user root
# Using Python version 3.6.8 (default, Nov 16 2020, 16:55:22) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
SnmpTagValue, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "SnmpTagValue")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Unsigned32, iso, Integer32, Counter32, Counter64, IpAddress, ModuleIdentity, mib_2, NotificationType, zeroDotZero, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Gauge32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Integer32", "Counter32", "Counter64", "IpAddress", "ModuleIdentity", "mib-2", "NotificationType", "zeroDotZero", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Gauge32", "TimeTicks", "Bits")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
dismanEventMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 88))
dismanEventMIB.setRevisions(('2000-10-16 00:00',))
if mibBuilder.loadTexts: dismanEventMIB.setLastUpdated('200010160000Z')
if mibBuilder.loadTexts: dismanEventMIB.setOrganization('IETF Distributed Management Working Group')
dismanEventMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 1))
mteResource = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 1, 1))
mteTrigger = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 1, 2))
mteObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 1, 3))
mteEvent = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 1, 4))
class FailureReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, -2, -3, -4, -5, -6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("localResourceLack", -1), ("badDestination", -2), ("destinationUnreachable", -3), ("noResponse", -4), ("badType", -5), ("sampleOverrun", -6), ("noError", 0), ("tooBig", 1), ("noSuchName", 2), ("badValue", 3), ("readOnly", 4), ("genErr", 5), ("noAccess", 6), ("wrongType", 7), ("wrongLength", 8), ("wrongEncoding", 9), ("wrongValue", 10), ("noCreation", 11), ("inconsistentValue", 12), ("resourceUnavailable", 13), ("commitFailed", 14), ("undoFailed", 15), ("authorizationError", 16), ("notWritable", 17), ("inconsistentName", 18))

mteResourceSampleMinimum = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteResourceSampleMinimum.setStatus('current')
mteResourceSampleInstanceMaximum = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 1, 2), Unsigned32()).setUnits('instances').setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteResourceSampleInstanceMaximum.setStatus('current')
mteResourceSampleInstances = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 1, 3), Gauge32()).setUnits('instances').setMaxAccess("readonly")
if mibBuilder.loadTexts: mteResourceSampleInstances.setStatus('current')
mteResourceSampleInstancesHigh = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 1, 4), Gauge32()).setUnits('instances').setMaxAccess("readonly")
if mibBuilder.loadTexts: mteResourceSampleInstancesHigh.setStatus('current')
mteResourceSampleInstanceLacks = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 1, 5), Counter32()).setUnits('instances').setMaxAccess("readonly")
if mibBuilder.loadTexts: mteResourceSampleInstanceLacks.setStatus('current')
mteTriggerFailures = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 2, 1), Counter32()).setUnits('failures').setMaxAccess("readonly")
if mibBuilder.loadTexts: mteTriggerFailures.setStatus('current')
mteTriggerTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 2, 2), )
if mibBuilder.loadTexts: mteTriggerTable.setStatus('current')
mteTriggerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1), ).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteTriggerName"))
if mibBuilder.loadTexts: mteTriggerEntry.setStatus('current')
mteOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: mteOwner.setStatus('current')
mteTriggerName = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: mteTriggerName.setStatus('current')
mteTriggerComment = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 3), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerComment.setStatus('current')
mteTriggerTest = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 4), Bits().clone(namedValues=NamedValues(("existence", 0), ("boolean", 1), ("threshold", 2))).clone(namedValues=NamedValues(("boolean", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerTest.setStatus('current')
mteTriggerSampleType = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2))).clone('absoluteValue')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerSampleType.setStatus('current')
mteTriggerValueID = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 6), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerValueID.setStatus('current')
mteTriggerValueIDWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerValueIDWildcard.setStatus('current')
mteTriggerTargetTag = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 8), SnmpTagValue().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerTargetTag.setStatus('current')
mteTriggerContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 9), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerContextName.setStatus('current')
mteTriggerContextNameWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerContextNameWildcard.setStatus('current')
mteTriggerFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 11), Unsigned32().clone(600)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerFrequency.setStatus('current')
mteTriggerObjectsOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 12), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerObjectsOwner.setStatus('current')
mteTriggerObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 13), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerObjects.setStatus('current')
mteTriggerEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerEnabled.setStatus('current')
mteTriggerEntryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteTriggerEntryStatus.setStatus('current')
mteTriggerDeltaTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 2, 3), )
if mibBuilder.loadTexts: mteTriggerDeltaTable.setStatus('current')
mteTriggerDeltaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1), ).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteTriggerName"))
if mibBuilder.loadTexts: mteTriggerDeltaEntry.setStatus('current')
sysUpTimeInstance = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 3, 0))
mteTriggerDeltaDiscontinuityID = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 1), ObjectIdentifier().clone((1, 3, 6, 1, 2, 1, 1, 3, 0))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerDeltaDiscontinuityID.setStatus('current')
mteTriggerDeltaDiscontinuityIDWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerDeltaDiscontinuityIDWildcard.setStatus('current')
mteTriggerDeltaDiscontinuityIDType = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("timeTicks", 1), ("timeStamp", 2), ("dateAndTime", 3))).clone('timeTicks')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerDeltaDiscontinuityIDType.setStatus('current')
mteTriggerExistenceTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 2, 4), )
if mibBuilder.loadTexts: mteTriggerExistenceTable.setStatus('current')
mteTriggerExistenceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1), ).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteTriggerName"))
if mibBuilder.loadTexts: mteTriggerExistenceEntry.setStatus('current')
mteTriggerExistenceTest = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 1), Bits().clone(namedValues=NamedValues(("present", 0), ("absent", 1), ("changed", 2))).clone(namedValues=NamedValues(("present", 0), ("absent", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerExistenceTest.setStatus('current')
mteTriggerExistenceStartup = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 2), Bits().clone(namedValues=NamedValues(("present", 0), ("absent", 1))).clone(namedValues=NamedValues(("present", 0), ("absent", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerExistenceStartup.setStatus('current')
mteTriggerExistenceObjectsOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerExistenceObjectsOwner.setStatus('current')
mteTriggerExistenceObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerExistenceObjects.setStatus('current')
mteTriggerExistenceEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerExistenceEventOwner.setStatus('current')
mteTriggerExistenceEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerExistenceEvent.setStatus('current')
mteTriggerBooleanTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 2, 5), )
if mibBuilder.loadTexts: mteTriggerBooleanTable.setStatus('current')
mteTriggerBooleanEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1), ).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteTriggerName"))
if mibBuilder.loadTexts: mteTriggerBooleanEntry.setStatus('current')
mteTriggerBooleanComparison = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unequal", 1), ("equal", 2), ("less", 3), ("lessOrEqual", 4), ("greater", 5), ("greaterOrEqual", 6))).clone('unequal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerBooleanComparison.setStatus('current')
mteTriggerBooleanValue = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerBooleanValue.setStatus('current')
mteTriggerBooleanStartup = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerBooleanStartup.setStatus('current')
mteTriggerBooleanObjectsOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerBooleanObjectsOwner.setStatus('current')
mteTriggerBooleanObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerBooleanObjects.setStatus('current')
mteTriggerBooleanEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerBooleanEventOwner.setStatus('current')
mteTriggerBooleanEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerBooleanEvent.setStatus('current')
mteTriggerThresholdTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 2, 6), )
if mibBuilder.loadTexts: mteTriggerThresholdTable.setStatus('current')
mteTriggerThresholdEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1), ).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteTriggerName"))
if mibBuilder.loadTexts: mteTriggerThresholdEntry.setStatus('current')
mteTriggerThresholdStartup = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rising", 1), ("falling", 2), ("risingOrFalling", 3))).clone('risingOrFalling')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdStartup.setStatus('current')
mteTriggerThresholdRising = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdRising.setStatus('current')
mteTriggerThresholdFalling = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdFalling.setStatus('current')
mteTriggerThresholdDeltaRising = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdDeltaRising.setStatus('current')
mteTriggerThresholdDeltaFalling = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdDeltaFalling.setStatus('current')
mteTriggerThresholdObjectsOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdObjectsOwner.setStatus('current')
mteTriggerThresholdObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdObjects.setStatus('current')
mteTriggerThresholdRisingEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdRisingEventOwner.setStatus('current')
mteTriggerThresholdRisingEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdRisingEvent.setStatus('current')
mteTriggerThresholdFallingEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdFallingEventOwner.setStatus('current')
mteTriggerThresholdFallingEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdFallingEvent.setStatus('current')
mteTriggerThresholdDeltaRisingEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 12), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdDeltaRisingEventOwner.setStatus('current')
mteTriggerThresholdDeltaRisingEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 13), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdDeltaRisingEvent.setStatus('current')
mteTriggerThresholdDeltaFallingEventOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 14), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdDeltaFallingEventOwner.setStatus('current')
mteTriggerThresholdDeltaFallingEvent = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 15), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteTriggerThresholdDeltaFallingEvent.setStatus('current')
mteObjectsTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 3, 1), )
if mibBuilder.loadTexts: mteObjectsTable.setStatus('current')
mteObjectsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1), ).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (0, "DISMAN-EVENT-MIB", "mteObjectsName"), (0, "DISMAN-EVENT-MIB", "mteObjectsIndex"))
if mibBuilder.loadTexts: mteObjectsEntry.setStatus('current')
mteObjectsName = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: mteObjectsName.setStatus('current')
mteObjectsIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: mteObjectsIndex.setStatus('current')
mteObjectsID = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 3), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteObjectsID.setStatus('current')
mteObjectsIDWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteObjectsIDWildcard.setStatus('current')
mteObjectsEntryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteObjectsEntryStatus.setStatus('current')
mteEventFailures = MibScalar((1, 3, 6, 1, 2, 1, 88, 1, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mteEventFailures.setStatus('current')
mteEventTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 4, 2), )
if mibBuilder.loadTexts: mteEventTable.setStatus('current')
mteEventEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1), ).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteEventName"))
if mibBuilder.loadTexts: mteEventEntry.setStatus('current')
mteEventName = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: mteEventName.setStatus('current')
mteEventComment = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 2), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteEventComment.setStatus('current')
mteEventActions = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 3), Bits().clone(namedValues=NamedValues(("notification", 0), ("set", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteEventActions.setStatus('current')
mteEventEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteEventEnabled.setStatus('current')
mteEventEntryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mteEventEntryStatus.setStatus('current')
mteEventNotificationTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 4, 3), )
if mibBuilder.loadTexts: mteEventNotificationTable.setStatus('current')
mteEventNotificationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1), ).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteEventName"))
if mibBuilder.loadTexts: mteEventNotificationEntry.setStatus('current')
mteEventNotification = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 1), ObjectIdentifier().clone((0, 0))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteEventNotification.setStatus('current')
mteEventNotificationObjectsOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteEventNotificationObjectsOwner.setStatus('current')
mteEventNotificationObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteEventNotificationObjects.setStatus('current')
mteEventSetTable = MibTable((1, 3, 6, 1, 2, 1, 88, 1, 4, 4), )
if mibBuilder.loadTexts: mteEventSetTable.setStatus('current')
mteEventSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1), ).setIndexNames((0, "DISMAN-EVENT-MIB", "mteOwner"), (1, "DISMAN-EVENT-MIB", "mteEventName"))
if mibBuilder.loadTexts: mteEventSetEntry.setStatus('current')
mteEventSetObject = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 1), ObjectIdentifier().clone((0, 0))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteEventSetObject.setStatus('current')
mteEventSetObjectWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteEventSetObjectWildcard.setStatus('current')
mteEventSetValue = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteEventSetValue.setStatus('current')
mteEventSetTargetTag = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 4), SnmpTagValue().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteEventSetTargetTag.setStatus('current')
mteEventSetContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 5), SnmpAdminString().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteEventSetContextName.setStatus('current')
mteEventSetContextNameWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mteEventSetContextNameWildcard.setStatus('current')
dismanEventMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 2))
dismanEventMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 2, 0))
dismanEventMIBNotificationObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 2, 1))
mteHotTrigger = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 1), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mteHotTrigger.setStatus('current')
mteHotTargetName = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mteHotTargetName.setStatus('current')
mteHotContextName = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 3), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mteHotContextName.setStatus('current')
mteHotOID = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 4), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mteHotOID.setStatus('current')
mteHotValue = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mteHotValue.setStatus('current')
mteFailedReason = MibScalar((1, 3, 6, 1, 2, 1, 88, 2, 1, 6), FailureReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mteFailedReason.setStatus('current')
mteTriggerFired = NotificationType((1, 3, 6, 1, 2, 1, 88, 2, 0, 1)).setObjects(("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotOID"), ("DISMAN-EVENT-MIB", "mteHotValue"))
if mibBuilder.loadTexts: mteTriggerFired.setStatus('current')
mteTriggerRising = NotificationType((1, 3, 6, 1, 2, 1, 88, 2, 0, 2)).setObjects(("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotOID"), ("DISMAN-EVENT-MIB", "mteHotValue"))
if mibBuilder.loadTexts: mteTriggerRising.setStatus('current')
mteTriggerFalling = NotificationType((1, 3, 6, 1, 2, 1, 88, 2, 0, 3)).setObjects(("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotOID"), ("DISMAN-EVENT-MIB", "mteHotValue"))
if mibBuilder.loadTexts: mteTriggerFalling.setStatus('current')
mteTriggerFailure = NotificationType((1, 3, 6, 1, 2, 1, 88, 2, 0, 4)).setObjects(("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotOID"), ("DISMAN-EVENT-MIB", "mteFailedReason"))
if mibBuilder.loadTexts: mteTriggerFailure.setStatus('current')
mteEventSetFailure = NotificationType((1, 3, 6, 1, 2, 1, 88, 2, 0, 5)).setObjects(("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotOID"), ("DISMAN-EVENT-MIB", "mteFailedReason"))
if mibBuilder.loadTexts: mteEventSetFailure.setStatus('current')
dismanEventMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 3))
dismanEventMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 3, 1))
dismanEventMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 88, 3, 2))
dismanEventMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 88, 3, 1, 1)).setObjects(("DISMAN-EVENT-MIB", "dismanEventResourceGroup"), ("DISMAN-EVENT-MIB", "dismanEventTriggerGroup"), ("DISMAN-EVENT-MIB", "dismanEventObjectsGroup"), ("DISMAN-EVENT-MIB", "dismanEventEventGroup"), ("DISMAN-EVENT-MIB", "dismanEventNotificationObjectGroup"), ("DISMAN-EVENT-MIB", "dismanEventNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dismanEventMIBCompliance = dismanEventMIBCompliance.setStatus('current')
dismanEventResourceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 1)).setObjects(("DISMAN-EVENT-MIB", "mteResourceSampleMinimum"), ("DISMAN-EVENT-MIB", "mteResourceSampleInstanceMaximum"), ("DISMAN-EVENT-MIB", "mteResourceSampleInstances"), ("DISMAN-EVENT-MIB", "mteResourceSampleInstancesHigh"), ("DISMAN-EVENT-MIB", "mteResourceSampleInstanceLacks"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dismanEventResourceGroup = dismanEventResourceGroup.setStatus('current')
dismanEventTriggerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 2)).setObjects(("DISMAN-EVENT-MIB", "mteTriggerFailures"), ("DISMAN-EVENT-MIB", "mteTriggerComment"), ("DISMAN-EVENT-MIB", "mteTriggerTest"), ("DISMAN-EVENT-MIB", "mteTriggerSampleType"), ("DISMAN-EVENT-MIB", "mteTriggerValueID"), ("DISMAN-EVENT-MIB", "mteTriggerValueIDWildcard"), ("DISMAN-EVENT-MIB", "mteTriggerTargetTag"), ("DISMAN-EVENT-MIB", "mteTriggerContextName"), ("DISMAN-EVENT-MIB", "mteTriggerContextNameWildcard"), ("DISMAN-EVENT-MIB", "mteTriggerFrequency"), ("DISMAN-EVENT-MIB", "mteTriggerObjectsOwner"), ("DISMAN-EVENT-MIB", "mteTriggerObjects"), ("DISMAN-EVENT-MIB", "mteTriggerEnabled"), ("DISMAN-EVENT-MIB", "mteTriggerEntryStatus"), ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityID"), ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityIDWildcard"), ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityIDType"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceTest"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceStartup"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceObjectsOwner"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceObjects"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerExistenceEvent"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanComparison"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanValue"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanStartup"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanObjectsOwner"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanObjects"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerBooleanEvent"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdStartup"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdObjectsOwner"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdObjects"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdRising"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdFalling"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRising"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFalling"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdRisingEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdRisingEvent"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdFallingEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdFallingEvent"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRisingEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRisingEvent"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFallingEventOwner"), ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFallingEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dismanEventTriggerGroup = dismanEventTriggerGroup.setStatus('current')
dismanEventObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 3)).setObjects(("DISMAN-EVENT-MIB", "mteObjectsID"), ("DISMAN-EVENT-MIB", "mteObjectsIDWildcard"), ("DISMAN-EVENT-MIB", "mteObjectsEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dismanEventObjectsGroup = dismanEventObjectsGroup.setStatus('current')
dismanEventEventGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 4)).setObjects(("DISMAN-EVENT-MIB", "mteEventFailures"), ("DISMAN-EVENT-MIB", "mteEventComment"), ("DISMAN-EVENT-MIB", "mteEventActions"), ("DISMAN-EVENT-MIB", "mteEventEnabled"), ("DISMAN-EVENT-MIB", "mteEventEntryStatus"), ("DISMAN-EVENT-MIB", "mteEventNotification"), ("DISMAN-EVENT-MIB", "mteEventNotificationObjectsOwner"), ("DISMAN-EVENT-MIB", "mteEventNotificationObjects"), ("DISMAN-EVENT-MIB", "mteEventSetObject"), ("DISMAN-EVENT-MIB", "mteEventSetObjectWildcard"), ("DISMAN-EVENT-MIB", "mteEventSetValue"), ("DISMAN-EVENT-MIB", "mteEventSetTargetTag"), ("DISMAN-EVENT-MIB", "mteEventSetContextName"), ("DISMAN-EVENT-MIB", "mteEventSetContextNameWildcard"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dismanEventEventGroup = dismanEventEventGroup.setStatus('current')
dismanEventNotificationObjectGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 5)).setObjects(("DISMAN-EVENT-MIB", "mteHotTrigger"), ("DISMAN-EVENT-MIB", "mteHotTargetName"), ("DISMAN-EVENT-MIB", "mteHotContextName"), ("DISMAN-EVENT-MIB", "mteHotOID"), ("DISMAN-EVENT-MIB", "mteHotValue"), ("DISMAN-EVENT-MIB", "mteFailedReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dismanEventNotificationObjectGroup = dismanEventNotificationObjectGroup.setStatus('current')
dismanEventNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 88, 3, 2, 6)).setObjects(("DISMAN-EVENT-MIB", "mteTriggerFired"), ("DISMAN-EVENT-MIB", "mteTriggerRising"), ("DISMAN-EVENT-MIB", "mteTriggerFalling"), ("DISMAN-EVENT-MIB", "mteTriggerFailure"), ("DISMAN-EVENT-MIB", "mteEventSetFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dismanEventNotificationGroup = dismanEventNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("DISMAN-EVENT-MIB", mteEventSetTargetTag=mteEventSetTargetTag, mteTriggerDeltaDiscontinuityIDType=mteTriggerDeltaDiscontinuityIDType, mteTrigger=mteTrigger, mteEventSetEntry=mteEventSetEntry, mteTriggerEntry=mteTriggerEntry, mteObjectsIndex=mteObjectsIndex, mteHotOID=mteHotOID, mteEventSetContextNameWildcard=mteEventSetContextNameWildcard, mteTriggerContextName=mteTriggerContextName, mteTriggerThresholdFallingEventOwner=mteTriggerThresholdFallingEventOwner, mteObjectsIDWildcard=mteObjectsIDWildcard, mteOwner=mteOwner, mteEventEntryStatus=mteEventEntryStatus, mteTriggerTargetTag=mteTriggerTargetTag, mteTriggerThresholdRisingEventOwner=mteTriggerThresholdRisingEventOwner, mteTriggerThresholdDeltaFalling=mteTriggerThresholdDeltaFalling, mteTriggerThresholdObjects=mteTriggerThresholdObjects, mteEventActions=mteEventActions, dismanEventResourceGroup=dismanEventResourceGroup, mteTriggerSampleType=mteTriggerSampleType, mteTriggerRising=mteTriggerRising, dismanEventMIBNotifications=dismanEventMIBNotifications, mteTriggerExistenceStartup=mteTriggerExistenceStartup, mteTriggerExistenceEvent=mteTriggerExistenceEvent, mteEventComment=mteEventComment, mteTriggerComment=mteTriggerComment, mteTriggerExistenceTable=mteTriggerExistenceTable, dismanEventNotificationObjectGroup=dismanEventNotificationObjectGroup, mteTriggerFrequency=mteTriggerFrequency, mteTriggerValueIDWildcard=mteTriggerValueIDWildcard, mteEventSetValue=mteEventSetValue, mteTriggerObjectsOwner=mteTriggerObjectsOwner, dismanEventMIBConformance=dismanEventMIBConformance, mteEventName=mteEventName, mteEventNotificationObjectsOwner=mteEventNotificationObjectsOwner, dismanEventTriggerGroup=dismanEventTriggerGroup, mteTriggerThresholdTable=mteTriggerThresholdTable, dismanEventEventGroup=dismanEventEventGroup, mteTriggerBooleanStartup=mteTriggerBooleanStartup, mteTriggerBooleanTable=mteTriggerBooleanTable, mteTriggerThresholdDeltaFallingEventOwner=mteTriggerThresholdDeltaFallingEventOwner, mteTriggerThresholdEntry=mteTriggerThresholdEntry, mteTriggerThresholdObjectsOwner=mteTriggerThresholdObjectsOwner, mteEventNotification=mteEventNotification, mteHotContextName=mteHotContextName, mteEvent=mteEvent, mteTriggerObjects=mteTriggerObjects, mteEventNotificationEntry=mteEventNotificationEntry, dismanEventMIB=dismanEventMIB, mteTriggerBooleanObjectsOwner=mteTriggerBooleanObjectsOwner, dismanEventMIBCompliances=dismanEventMIBCompliances, mteTriggerExistenceEntry=mteTriggerExistenceEntry, mteHotValue=mteHotValue, mteEventSetContextName=mteEventSetContextName, mteResourceSampleMinimum=mteResourceSampleMinimum, mteTriggerThresholdFallingEvent=mteTriggerThresholdFallingEvent, mteObjects=mteObjects, mteEventNotificationObjects=mteEventNotificationObjects, mteTriggerThresholdStartup=mteTriggerThresholdStartup, mteTriggerDeltaDiscontinuityIDWildcard=mteTriggerDeltaDiscontinuityIDWildcard, mteTriggerThresholdFalling=mteTriggerThresholdFalling, mteEventNotificationTable=mteEventNotificationTable, mteHotTrigger=mteHotTrigger, mteTriggerName=mteTriggerName, dismanEventMIBNotificationObjects=dismanEventMIBNotificationObjects, mteTriggerFailure=mteTriggerFailure, mteEventSetFailure=mteEventSetFailure, mteTriggerExistenceEventOwner=mteTriggerExistenceEventOwner, mteTriggerFired=mteTriggerFired, PYSNMP_MODULE_ID=dismanEventMIB, mteTriggerDeltaDiscontinuityID=mteTriggerDeltaDiscontinuityID, mteTriggerFailures=mteTriggerFailures, mteTriggerExistenceObjects=mteTriggerExistenceObjects, mteTriggerThresholdDeltaRisingEventOwner=mteTriggerThresholdDeltaRisingEventOwner, mteEventFailures=mteEventFailures, mteFailedReason=mteFailedReason, FailureReason=FailureReason, mteObjectsEntryStatus=mteObjectsEntryStatus, mteTriggerBooleanValue=mteTriggerBooleanValue, mteTriggerExistenceObjectsOwner=mteTriggerExistenceObjectsOwner, mteTriggerThresholdDeltaFallingEvent=mteTriggerThresholdDeltaFallingEvent, mteResourceSampleInstanceLacks=mteResourceSampleInstanceLacks, mteTriggerDeltaTable=mteTriggerDeltaTable, mteObjectsName=mteObjectsName, mteTriggerBooleanEventOwner=mteTriggerBooleanEventOwner, mteTriggerEntryStatus=mteTriggerEntryStatus, mteTriggerBooleanEntry=mteTriggerBooleanEntry, mteTriggerTest=mteTriggerTest, dismanEventMIBGroups=dismanEventMIBGroups, mteTriggerExistenceTest=mteTriggerExistenceTest, mteTriggerBooleanComparison=mteTriggerBooleanComparison, dismanEventMIBCompliance=dismanEventMIBCompliance, mteEventSetObject=mteEventSetObject, dismanEventNotificationGroup=dismanEventNotificationGroup, mteTriggerThresholdDeltaRisingEvent=mteTriggerThresholdDeltaRisingEvent, dismanEventMIBObjects=dismanEventMIBObjects, mteTriggerBooleanEvent=mteTriggerBooleanEvent, mteHotTargetName=mteHotTargetName, mteResourceSampleInstanceMaximum=mteResourceSampleInstanceMaximum, mteEventEnabled=mteEventEnabled, mteResourceSampleInstancesHigh=mteResourceSampleInstancesHigh, mteObjectsTable=mteObjectsTable, mteTriggerValueID=mteTriggerValueID, mteObjectsEntry=mteObjectsEntry, mteTriggerThresholdDeltaRising=mteTriggerThresholdDeltaRising, mteEventTable=mteEventTable, mteResourceSampleInstances=mteResourceSampleInstances, mteTriggerThresholdRisingEvent=mteTriggerThresholdRisingEvent, mteTriggerTable=mteTriggerTable, mteTriggerContextNameWildcard=mteTriggerContextNameWildcard, mteEventSetObjectWildcard=mteEventSetObjectWildcard, mteEventSetTable=mteEventSetTable, mteTriggerThresholdRising=mteTriggerThresholdRising, mteEventEntry=mteEventEntry, mteTriggerBooleanObjects=mteTriggerBooleanObjects, mteTriggerFalling=mteTriggerFalling, mteTriggerDeltaEntry=mteTriggerDeltaEntry, dismanEventObjectsGroup=dismanEventObjectsGroup, mteObjectsID=mteObjectsID, mteResource=mteResource, mteTriggerEnabled=mteTriggerEnabled, dismanEventMIBNotificationPrefix=dismanEventMIBNotificationPrefix, sysUpTimeInstance=sysUpTimeInstance)
