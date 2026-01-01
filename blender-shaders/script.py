import random

import bpy


def create_procedural_material(mat_name):
    mat = bpy.data.materials.new(name=mat_name)

    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    nodes.clear()

    node_output = nodes.new(type="ShaderNodeOutputMaterial")
    node_output.location = (400, 0)

    node_principled = nodes.new(type="ShaderNodeBsdfPrincipled")
    node_principled.location = (0, 0)

    node_principled.inputs["Roughness"].default_value = 0.2
    node_principled.inputs["Metallic"].default_value = 1.0

    node_noise = nodes.new(type="ShaderNodeTexNoise")
    node_noise.location = (-600, 0)
    node_noise.inputs["Scale"].default_value = 15.0
    node_noise.inputs["Detail"].default_value = 10.0

    node_ramp = nodes.new(type="ShaderNodeValToRGB")
    node_ramp.location = (-300, 0)

    node_ramp.color_ramp.elements[0].color = (0.1, 0.1, 0.1, 1)

    rand_r = random.random()
    rand_g = random.random()
    rand_b = random.random()
    node_ramp.color_ramp.elements[1].color = (rand_r, rand_g, rand_b, 1)

    links.new(node_noise.outputs["Fac"], node_ramp.inputs["Fac"])

    links.new(node_ramp.outputs["Color"], node_principled.inputs["Base Color"])

    links.new(node_principled.outputs["BSDF"], node_output.inputs["Surface"])

    return mat


my_new_mat = create_procedural_material("SciFi_Metal_Random")

bpy.context.object.data.materials.append(my_new_mat)
