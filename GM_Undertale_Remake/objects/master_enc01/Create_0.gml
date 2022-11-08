//create player and enemy
instance_create_layer(room_width/2, enemy_height/2, "fight", enemy)
instance_create_layer(room_width/2-50, room_height/2, "fight", player)

//create the butttons 
instance_create_layer(room_width/2-button_width, room_height/2+playframe_height/2+button_margin, "buttons", obj_button_fight_trained_AI)
instance_create_layer(room_width/2-button_width, room_height/2+playframe_height/2+2*button_margin+button_height, "buttons", obj_button_fight_untrained_AI)
instance_create_layer(room_width/2+button_width, room_height/2+playframe_height/2+button_margin, "buttons", obj_button_act)

//create the walls of the playing field
instance_create_layer(room_width/2, room_height/2, "walls", playframe_bottom);
instance_create_layer(room_width/2, room_height/2, "walls", playframe_top);
instance_create_layer(room_width/2, room_height/2, "walls", playframe_left);
instance_create_layer(room_width/2, room_height/2, "walls", playframe_right);

//create mapping graphic in bottom left corner
instance_create_layer(0, room_height, "user_info", text_box)

//create heart counter
self.lives = 3
instance_create_layer(room_width/3, room_height/3, "user_info", heartcounter_heart)

//randomize the seed for randomly generating things
randomize()