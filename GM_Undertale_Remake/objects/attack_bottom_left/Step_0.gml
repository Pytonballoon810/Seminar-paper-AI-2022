step = step + 1

if step > 30
{
	image_index = 1
}
if step >= 90
{
	instance_destroy(self);
	enemy.attack_finished = true
	if enemy.trained
{
	with(enemy){event_user(0);};
}else with(enemy){event_user(1);};
}
