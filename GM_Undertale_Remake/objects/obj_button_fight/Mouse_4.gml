with(btn_master){event_user(0);}

instance_create_layer(room_width/2, room_height/2, "walls", playframe_bottom)
instance_create_layer(room_width/2, room_height/2, "walls", playframe_top)
instance_create_layer(room_width/2, room_height/2, "walls", playframe_left)
instance_create_layer(room_width/2, room_height/2, "walls", playframe_right)

obj_button_fight.visible = false
obj_button_act.visible = false