# get/set trasformation matrix

import maya.api.OpenMaya as om

mSel = om.MGlobal.getActiveSelectionList()

if not mSel.isEmpty():
  mObj = mSel.getDependNode(0)
  if mObj.hasFn(om.MFn.kDagNode):
    mDagPath = mSel.getDagPath(0)
    transformFn = om.MFnTransform(mDagPath)
    inverseMatrix = mDagPath.inclusiveMatrixInverse()
    transformationMatrix = om.MTransformationMatrix(inverseMatrix)
    transformFn.setTransformation(transformationMatrix)
