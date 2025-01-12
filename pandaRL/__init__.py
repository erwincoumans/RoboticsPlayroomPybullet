from gym.envs.registration import register

register(
    id='pandaReach-v0',
    entry_point='pandaRL.envs:pandaReach',
)

register(
    id='pandaReach2D-v0',
    entry_point='pandaRL.envs:pandaReach2D',
)

register(
    id='pointMass3D-v0',
    entry_point='pandaRL.envs:pointMassEnv',
)

register(
    id='pandaPush-v0',
    entry_point='pandaRL.envs:pandaPush',
)

register(
    id='pandaPick-v0',
    entry_point='pandaRL.envs:pandaPick',
)

register(
    id='pandaPlay-v0',
    entry_point='pandaRL.envs:pandaPlay',
)
register(
    id='pandaPlay1Obj-v0',
    entry_point='pandaRL.envs:pandaPlay1Obj',
)
register(
    id='pandaPlayRel1Obj-v0',
    entry_point='pandaRL.envs:pandaPlayRel1Obj',
)
register(
    id='pandaPlayJoints-v0',
    entry_point='pandaRL.envs:pandaPlayRelJoints',
)

register(
    id='pandaPlayRelJoints1Obj-v0',
    entry_point='pandaRL.envs:pandaPlayRelJoints1Obj',
)

register(
    id='pandaPlayAbsJoints1Obj-v0',
    entry_point='pandaRL.envs:pandaPlayAbsJoints1Obj',
)

register(
    id='pandaPlayAbsRPY1Obj-v0',
    entry_point='pandaRL.envs:pandaPlayAbsRPY1Obj',
)

register(
    id='pandaPlayRelRPY1Obj-v0',
    entry_point='pandaRL.envs:pandaPlayRelRPY1Obj',
)


register(
    id='UR5Play1Obj-v0',
    entry_point='pandaRL.envs:UR5Play1Obj',
)

register(
    id='UR5PlayRel1Obj-v0',
    entry_point='pandaRL.envs:UR5PlayRel1Obj',
)

register(
    id='UR5PlayRelJoints1Obj-v0',
    entry_point='pandaRL.envs:UR5PlayRelJoints1Obj',
)

register(
    id='UR5PlayAbsJoints1Obj-v0',
    entry_point='pandaRL.envs:UR5PlayAbsJoints1Obj',
)

register(
    id='UR5PlayAbsRPY1Obj-v0',
    entry_point='pandaRL.envs:UR5PlayAbsRPY1Obj',
)

register(
    id='UR5PlayRelRPY1Obj-v0',
    entry_point='pandaRL.envs:UR5PlayRelRPY1Obj',
)