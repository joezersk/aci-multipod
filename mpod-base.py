#!/usr/bin/env python

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.bgp
import cobra.model.ctrlr
import cobra.model.dbg
import cobra.model.fabric
import cobra.model.fv
import cobra.model.l3ext
import cobra.model.ospf
import cobra.model.pol
from cobra.internal.codec.xmlcodec import toXMLStr

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://1.1.1.1', 'admin', 'cisco123')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
topMo = cobra.model.pol.Uni('')

# build the request using cobra syntax
fabricInst = cobra.model.fabric.Inst(topMo)
dbgOngoingAcMode = cobra.model.dbg.OngoingAcMode(fabricInst, mode='path', name='default')

c = cobra.mit.request.ConfigRequest()
c.addMo(fabricInst)
md.commit(c)

fvTenant = cobra.model.fv.Tenant(topMo, name='infra')
fvFabricExtConnP = cobra.model.fv.FabricExtConnP(fvTenant, rt='extended:as2-nn4:11:22', id='1', name='fabricExtConnPolName_9a92763eadbe259d')
fvPodConnP = cobra.model.fv.PodConnP(fvFabricExtConnP, id='2')
fvIp = cobra.model.fv.Ip(fvPodConnP, addr='200.1.1.1/32')
fvPodConnP2 = cobra.model.fv.PodConnP(fvFabricExtConnP, id='1')
fvIp2 = cobra.model.fv.Ip(fvPodConnP2, addr='100.1.1.1/32')
l3extFabricExtRoutingP = cobra.model.l3ext.FabricExtRoutingP(fvFabricExtConnP, name='MPOD_EXT_ROUTE_PROFILE')
l3extSubnet = cobra.model.l3ext.Subnet(l3extFabricExtRoutingP, ip='202.1.0.0/16')
l3extSubnet2 = cobra.model.l3ext.Subnet(l3extFabricExtRoutingP, ip='203.1.0.0/16')
fvPeeringP = cobra.model.fv.PeeringP(fvFabricExtConnP, type='automatic_with_full_mesh')
ospfIfPol = cobra.model.ospf.IfPol(fvTenant, nwT='p2p', pfxSuppress='inherit', name='MPOD_OSPF_P2P', prio='1', ctrl='advert-subnet,mtu-ignore', helloIntvl='10', rexmitIntvl='5', xmitDelay='1', cost='unspecified', deadIntvl='40')
l3extOut = cobra.model.l3ext.Out(fvTenant, name='MPOD_OSPF_OUT', enforceRtctrl='export', targetDscp='unspecified')
l3extRsEctx = cobra.model.l3ext.RsEctx(l3extOut, tnFvCtxName='overlay-1')
l3extLNodeP = cobra.model.l3ext.LNodeP(l3extOut, tag='yellow-green', name='MPOD_OSPF_NODES', targetDscp='unspecified')
l3extRsNodeL3OutAtt = cobra.model.l3ext.RsNodeL3OutAtt(l3extLNodeP, tDn='topology/pod-2/node-202', rtrId='222.222.222.222', rtrIdLoopBack='yes')
l3extInfraNodeP = cobra.model.l3ext.InfraNodeP(l3extRsNodeL3OutAtt, fabricExtCtrlPeering='yes')
l3extLoopBackIfP = cobra.model.l3ext.LoopBackIfP(l3extRsNodeL3OutAtt, addr='222.222.222.222')
l3extRsNodeL3OutAtt2 = cobra.model.l3ext.RsNodeL3OutAtt(l3extLNodeP, tDn='topology/pod-1/node-201', rtrId='111.111.111.111', rtrIdLoopBack='yes')
l3extInfraNodeP2 = cobra.model.l3ext.InfraNodeP(l3extRsNodeL3OutAtt2, fabricExtCtrlPeering='yes')
l3extLoopBackIfP2 = cobra.model.l3ext.LoopBackIfP(l3extRsNodeL3OutAtt2, addr='111.111.111.111')
l3extLIfP = cobra.model.l3ext.LIfP(l3extLNodeP, tag='yellow-green', name='MPOD_OSPF_INTS')
ospfIfP = cobra.model.ospf.IfP(l3extLIfP, authKeyId='1', authType='none')
ospfRsIfPol = cobra.model.ospf.RsIfPol(ospfIfP, tnOspfIfPolName='MPOD_OSPF_P2P')
l3extRsNdIfPol = cobra.model.l3ext.RsNdIfPol(l3extLIfP)
l3extRsIngressQosDppPol = cobra.model.l3ext.RsIngressQosDppPol(l3extLIfP)
l3extRsEgressQosDppPol = cobra.model.l3ext.RsEgressQosDppPol(l3extLIfP)
l3extRsPathL3OutAtt = cobra.model.l3ext.RsPathL3OutAtt(l3extLIfP, tDn='topology/pod-2/paths-202/pathep-[eth1/20]', targetDscp='unspecified', encapScope='local', llAddr='::', mac='00:22:BD:F8:19:FF', mode='regular', encap='vlan-4', ifInstT='sub-interface', mtu='inherit', addr='203.1.1.1/30')
l3extRsPathL3OutAtt2 = cobra.model.l3ext.RsPathL3OutAtt(l3extLIfP, tDn='topology/pod-1/paths-201/pathep-[eth1/20]', targetDscp='unspecified', encapScope='local', llAddr='::', mac='00:22:BD:F8:19:FF', mode='regular', encap='vlan-4', ifInstT='sub-interface', mtu='inherit', addr='202.1.1.1/30')
l3extInstP = cobra.model.l3ext.InstP(l3extOut, matchT='AtleastOne', name='l3extInstPNamee75ff0551285bf11', prio='unspecified', targetDscp='unspecified')
fvRsCustQosPol = cobra.model.fv.RsCustQosPol(l3extInstP)
bgpExtP = cobra.model.bgp.ExtP(l3extOut)
ospfExtP = cobra.model.ospf.ExtP(l3extOut, areaCtrl='redistribute,summary', areaType='regular', areaCost='1', areaId='backbone')

c = cobra.mit.request.ConfigRequest()
c.addMo(fvTenant)
md.commit(c)


ctrlrInst = cobra.model.ctrlr.Inst(topMo)
fabricSetupPol = cobra.model.fabric.SetupPol(ctrlrInst, name='default')
fabricSetupP = cobra.model.fabric.SetupP(fabricSetupPol, tepPool='10.1.0.0/16', podId='2')


# commit the generated code to APIC
#print toXMLStr(topMo)
c = cobra.mit.request.ConfigRequest()
c.addMo(ctrlrInst)
md.commit(c)

