import bpy
import bmesh
import math
import json


def main(context):
    
#    for ob in context.scene.objects:
#        print(ob)
        
    collection = bpy.data.collections["AtoZ"]

    num = 1
    
    for obj in collection.objects:
        print(obj)
        print(num)
        # obj.hide_viewport = False
        # obj.hide_render = False

        # bpy.context.scene.render.filepath = 'C:\\Users\\kirkl\\Desktop\\web3\\AtoZ\\image\\' + str(num) + '.png'
        # bpy.ops.render.render(write_still=True)
        # num+=1
        # obj.hide_viewport = True
        # obj.hide_render = True

    
        meta_data_dict = {
        "name": obj.name,
        "description": "A letter of the alphabet with special powers",
        "image": 'https://raw.githubusercontent.com/smarthug/AtoZ/master/image/' + str(num) + '.png',
        "attributes": [
            {
                "trait_type": "character",
                "value": obj.name
            },
            {
                "trait_type": "color",
                "value": "white"
            },
        ]
        }
        # file_name = obj.name + '.png'
        json_metadata = json.dumps(meta_data_dict, indent=1, ensure_ascii=True)
        with open('C:\\Users\\kirkl\\Desktop\\web3\\AtoZ\\json\\' + str(num) + '.json', 'w') as outfile:
            outfile.write(json_metadata +'\n')
        num+=1
    # Iterate through the alphabet string
#    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#        print(char)
        
#        font_curve = bpy.data.curves.new(type="FONT", name="Font Curve")
#        font_curve.body = char
#        font_obj = bpy.data.objects.new(name="Font Object", object_data=font_curve)
#        font_obj.name = char
#        font_obj.rotation_euler = [math.pi/ 2, 0, 0]
#        font_obj.data.extrude = 0.1
#        font_obj.origin_set(type="ORIGIN_CENTER_OF_VOLUME", )
#        font_obj.location_clear()
#     #    bpy.context.scene.collection.objects.link(font_obj)
#        collection.objects.link(font_obj)

      
 



class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.simple_operator()
