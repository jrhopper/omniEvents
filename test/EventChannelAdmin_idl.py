# Python stubs generated by omniidl from ../idl/EventChannelAdmin.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(2,0, __file__)

# #include "CosNaming.idl"
import CosNaming_idl
_0_CosNaming = omniORB.openModule("CosNaming")
_0_CosNaming__POA = omniORB.openModule("CosNaming__POA")
# #include "CosLifeCycle.idl"
import CosLifeCycle_idl
_0_CosLifeCycle = omniORB.openModule("CosLifeCycle")
_0_CosLifeCycle__POA = omniORB.openModule("CosLifeCycle__POA")

#
# Start of module "EventChannelAdmin"
#
__name__ = "EventChannelAdmin"
_0_EventChannelAdmin = omniORB.openModule("EventChannelAdmin", r"../idl/EventChannelAdmin.idl")
_0_EventChannelAdmin__POA = omniORB.openModule("EventChannelAdmin__POA", r"../idl/EventChannelAdmin.idl")


# interface EventChannelFactory
_0_EventChannelAdmin._d_EventChannelFactory = (omniORB.tcInternal.tv_objref, "IDL:EventChannelAdmin/EventChannelFactory:1.0", "EventChannelFactory")
omniORB.typeMapping["IDL:EventChannelAdmin/EventChannelFactory:1.0"] = _0_EventChannelAdmin._d_EventChannelFactory
_0_EventChannelAdmin.EventChannelFactory = omniORB.newEmptyClass()
class EventChannelFactory (_0_CosLifeCycle.GenericFactory):
    _NP_RepositoryId = _0_EventChannelAdmin._d_EventChannelFactory[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_EventChannelAdmin.EventChannelFactory = EventChannelFactory
_0_EventChannelAdmin._tc_EventChannelFactory = omniORB.tcInternal.createTypeCode(_0_EventChannelAdmin._d_EventChannelFactory)
omniORB.registerType(EventChannelFactory._NP_RepositoryId, _0_EventChannelAdmin._d_EventChannelFactory, _0_EventChannelAdmin._tc_EventChannelFactory)

# EventChannelFactory object reference
class _objref_EventChannelFactory (_0_CosLifeCycle._objref_GenericFactory):
    _NP_RepositoryId = EventChannelFactory._NP_RepositoryId

    def __init__(self):
        _0_CosLifeCycle._objref_GenericFactory.__init__(self)

    __methods__ = [] + _0_CosLifeCycle._objref_GenericFactory.__methods__

omniORB.registerObjref(EventChannelFactory._NP_RepositoryId, _objref_EventChannelFactory)
_0_EventChannelAdmin._objref_EventChannelFactory = _objref_EventChannelFactory
del EventChannelFactory, _objref_EventChannelFactory

# EventChannelFactory skeleton
__name__ = "EventChannelAdmin__POA"
class EventChannelFactory (_0_CosLifeCycle__POA.GenericFactory):
    _NP_RepositoryId = _0_EventChannelAdmin.EventChannelFactory._NP_RepositoryId


    _omni_op_d = {}
    _omni_op_d.update(_0_CosLifeCycle__POA.GenericFactory._omni_op_d)

EventChannelFactory._omni_skeleton = EventChannelFactory
_0_EventChannelAdmin__POA.EventChannelFactory = EventChannelFactory
del EventChannelFactory
__name__ = "EventChannelAdmin"

#
# End of module "EventChannelAdmin"
#
__name__ = "EventChannelAdmin_idl"

_exported_modules = ( "EventChannelAdmin", )

# The end.
