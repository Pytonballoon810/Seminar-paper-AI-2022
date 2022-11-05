instance_create_layer(room_width/2, room_height/2, "walls", playframe_bottom)
instance_create_layer(room_width/2, room_height/2, "walls", playframe_top)
instance_create_layer(room_width/2, room_height/2, "walls", playframe_left)
instance_create_layer(room_width/2, room_height/2, "walls", playframe_right)

instance_create_layer(room_width/2, enemy_height/2, "fight", enemy)
instance_create_layer(room_width/2-50, room_height/2, "fight", player)

instance_create_layer(room_width/2-button_width, room_height/2+playframe_height/2+button_margin, "buttons", obj_button_fight)
instance_create_layer(room_width/2+button_width, room_height/2+playframe_height/2+button_margin, "buttons", obj_button_act)
