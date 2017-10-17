# aci-multipod
<P>
There are four files here in two logical groups.   The two text files are the running configs of my IPN Nexus 9200 series standlone switches.  Use these as example to build up your own IPN devices.  Key areas to look at are setting up PIM, DHCP-Relay, MTU of 9150, and OSPF.
<P>
<B>UPDATE OCT 2017</B>
<P>
<I>The response to my multipod videos and this repo has grown beyond my intial expectations and I am truly flattered.  That is good news for ACI but it brings a problem too.  The configs you see here are examples only.  What is germaine to my own lab and config style might not exactly match your environment.  My only sincere request is not to take what you find here verbatim, but use it, and review the configs in the context of your own setup and make appropiate decisons to adapt it for what works for you.  Ask questions!  Does this config make sense for me?  Should I use a different mask, etc etc.
<P>
I also uploaded a PCAP file that captures the DHCP exchange when discovering the first spine in a remote pod.  
</I>
<P>
<HR>
<P>
<B>UPDATE DEC 2016</B>
<P>
<I>I have updated my IPN config to use an optional (but recommended) vrf just for the multipod stuff.  Please review the running config files in version 2 in this repo.  Also note some PIM commands now moved to the dedicated vrf context.</I>
<P>
<HR>
<P>
The two python scripts are those used in my own lab to setup the OSPF adjacency to IPN (<B>mpod-base.py</B>) and the other to setup the physical front-panel ports (i.e complete the MP-BGP control plane) on the ACI fabric used by the spines towards the IPN (<B>mpod-phys.py</B>).  Please note that the scripts use values that are <b>specific to my own setup</b>.  You will need to edit them to match the ports, ip addresses and settings in your own environment.  
<P>
Also, you must have already installed the <a href="https://developer.cisco.com/media/apicDcPythonAPI_v0.1/install.html">ACI COBRA SDK</a> on the system where you will run this.




