if enemy.trained
{
	with(enemy){event_user(0);};
}else with(enemy){event_user(1);};
instance_destroy(self)