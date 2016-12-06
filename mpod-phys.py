#!/usr/bin/env python

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.bgp
import cobra.model.dhcp
import cobra.model.fabric
import cobra.model.fv
import cobra.model.fvns
import cobra.model.infra
import cobra.model.l3ext
import cobra.model.pol
from cobra.internal.codec.xmlcodec import toXMLStr

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://1.1.1.1', 'admin', 'cisco123')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
topMo = cobra.model.pol.Uni('')

# build the request using cobra syntax
infraInfra = cobra.model.infra.Infra(topMo)
infraFuncP = cobra.model.infra.FuncP(infraInfra, name='default')
infraSpAccPortGrp = cobra.model.infra.SpAccPortGrp(infraFuncP, name='MPOD-SPINE2-PG')
infraRsCdpIfPol = cobra.model.infra.RsCdpIfPol(infraSpAccPortGrp)
infraRsAttEntP = cobra.model.infra.RsAttEntP(infraSpAccPortGrp, tDn='uni/infra/attentp-MPOD_AAEP')
infraRsHIfPol = cobra.model.infra.RsHIfPol(infraSpAccPortGrp)
infraSpAccPortGrp2 = cobra.model.infra.SpAccPortGrp(infraFuncP, name='MPOD-SPINE1-PG')
infraRsCdpIfPol2 = cobra.model.infra.RsCdpIfPol(infraSpAccPortGrp2)
infraRsAttEntP2 = cobra.model.infra.RsAttEntP(infraSpAccPortGrp2, tDn='uni/infra/attentp-MPOD_AAEP')
infraRsHIfPol2 = cobra.model.infra.RsHIfPol(infraSpAccPortGrp2)
fvnsVlanInstP = cobra.model.fvns.VlanInstP(infraInfra, name='MPOD_VLANS', allocMode='static')
fvnsEncapBlk = cobra.model.fvns.EncapBlk(fvnsVlanInstP, to='vlan-4', from_='vlan-4', allocMode='inherit')
infraAttEntityP = cobra.model.infra.AttEntityP(infraInfra, name='MPOD_AAEP')
infraProvAcc = cobra.model.infra.ProvAcc(infraAttEntityP, name='provacc')
dhcpInfraProvP = cobra.model.dhcp.InfraProvP(infraProvAcc, mode='controller')
infraRsFuncToEpg = cobra.model.infra.RsFuncToEpg(infraProvAcc, mode='regular', tDn='uni/tn-infra/ap-access/epg-default', encap='vlan-3456', primaryEncap='unknown')
infraRsDomP = cobra.model.infra.RsDomP(infraAttEntityP, tDn='uni/l3dom-MPOD_L3_DOMAIN')
infraSpineP = cobra.model.infra.SpineP(infraInfra, name='MPOD-S2-SWITCH')
infraSpineS = cobra.model.infra.SpineS(infraSpineP, type='range', name='SPINE2')
infraNodeBlk = cobra.model.infra.NodeBlk(infraSpineS, from_='202', name='05183e5184f05c0e', to_='202')
infraRsSpAccPortP = cobra.model.infra.RsSpAccPortP(infraSpineP, tDn='uni/infra/spaccportprof-MPOD-S2-ETH20')
infraSpineP2 = cobra.model.infra.SpineP(infraInfra, name='MPOD-S1-SWITCH')
infraSpineS2 = cobra.model.infra.SpineS(infraSpineP2, type='range', name='SPINE1')
infraNodeBlk2 = cobra.model.infra.NodeBlk(infraSpineS2, from_='201', name='7eb0b8ef28c813b6', to_='201')
infraRsSpAccPortP2 = cobra.model.infra.RsSpAccPortP(infraSpineP2, tDn='uni/infra/spaccportprof-MPOD-S1-ETH20')
infraSpAccPortP = cobra.model.infra.SpAccPortP(infraInfra, name='MPOD-S2-ETH20')
infraSHPortS = cobra.model.infra.SHPortS(infraSpAccPortP, type='range', name='ETH1-20')
infraPortBlk = cobra.model.infra.PortBlk(infraSHPortS, name='block2', fromPort='20', fromCard='1', toPort='20', toCard='1')
infraRsSpAccGrp = cobra.model.infra.RsSpAccGrp(infraSHPortS, tDn='uni/infra/funcprof/spaccportgrp-MPOD-SPINE2-PG')
infraSpAccPortP2 = cobra.model.infra.SpAccPortP(infraInfra, name='MPOD-S1-ETH20')
infraSHPortS2 = cobra.model.infra.SHPortS(infraSpAccPortP2, type='range', name='ETH1_20')
infraPortBlk2 = cobra.model.infra.PortBlk(infraSHPortS2, name='block2', fromPort='20', fromCard='1', toPort='20', toCard='1')
infraRsSpAccGrp2 = cobra.model.infra.RsSpAccGrp(infraSHPortS2, tDn='uni/infra/funcprof/spaccportgrp-MPOD-SPINE1-PG')


c = cobra.mit.request.ConfigRequest()
c.addMo(infraInfra)
md.commit(c)

fvTenant = cobra.model.fv.Tenant(topMo, name='infra')
l3extOut = cobra.model.l3ext.Out(fvTenant, name='MPOD_OSPF_OUT', enforceRtctrl='export', targetDscp='unspecified')
l3extRsL3DomAtt = cobra.model.l3ext.RsL3DomAtt(l3extOut, tDn='uni/l3dom-MPOD_L3_DOMAIN')

c = cobra.mit.request.ConfigRequest()
c.addMo(fvTenant)
md.commit(c)

fabricInst = cobra.model.fabric.Inst(topMo)
fabricFuncP = cobra.model.fabric.FuncP(fabricInst)
fabricPodPGrp = cobra.model.fabric.PodPGrp(fabricFuncP, name='HOUSEKEEPING_GROUP')
fabricRsPodPGrpIsisDomP = cobra.model.fabric.RsPodPGrpIsisDomP(fabricPodPGrp)
fabricRsPodPGrpBGPRRP = cobra.model.fabric.RsPodPGrpBGPRRP(fabricPodPGrp, tnBgpInstPolName='default')
fabricRsTimePol = cobra.model.fabric.RsTimePol(fabricPodPGrp)
fabricRsCommPol = cobra.model.fabric.RsCommPol(fabricPodPGrp)
fabricRsPodPGrpCoopP = cobra.model.fabric.RsPodPGrpCoopP(fabricPodPGrp)
fabricRsSnmpPol = cobra.model.fabric.RsSnmpPol(fabricPodPGrp)
bgpInstPol = cobra.model.bgp.InstPol(fabricInst, name='default')
bgpRRP = cobra.model.bgp.RRP(bgpInstPol)
bgpRRNodePEp = cobra.model.bgp.RRNodePEp(bgpRRP, id='202', podId='1')
bgpRRNodePEp2 = cobra.model.bgp.RRNodePEp(bgpRRP, id='201', podId='1')
bgpAsP = cobra.model.bgp.AsP(bgpInstPol, asn='65001')
fabricPodP = cobra.model.fabric.PodP(fabricInst, name='default')
fabricPodS = cobra.model.fabric.PodS(fabricPodP, type='ALL', name='default')
fabricRsPodPGrp = cobra.model.fabric.RsPodPGrp(fabricPodS, tDn='uni/fabric/funcprof/podpgrp-HOUSEKEEPING_GROUP')

c = cobra.mit.request.ConfigRequest()
c.addMo(fabricInst)
md.commit(c)

l3extDomP = cobra.model.l3ext.DomP(topMo, name='MPOD_L3_DOMAIN')
infraRsVlanNs = cobra.model.infra.RsVlanNs(l3extDomP, tDn='uni/infra/vlanns-[MPOD_VLANS]-static')


# commit the generated code to APIC
#print toXMLStr(topMo)
c = cobra.mit.request.ConfigRequest()
c.addMo(l3extDomP)
md.commit(c)

