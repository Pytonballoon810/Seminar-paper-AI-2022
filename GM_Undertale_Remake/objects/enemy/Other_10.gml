// workaround for trained AI algorithm

if attacks < attacks_per_round
{	
		attacks += 1
		attack_finished = false
		alarm[0] = attack_intervall*room_speed;

}else
{
	self.attacks = 0
	obj_button_fight_trained_AI.visible = true
	obj_button_fight_untrained_AI.visible = true
	obj_button_act.visible = true
}