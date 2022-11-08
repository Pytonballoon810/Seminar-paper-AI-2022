// loop for attacking and main attacking logic (trained)

x_off = room_width/2-playframe_bottom.sprite_width/2
y_off = room_height/2-playframe_bottom.sprite_height/2

if player.x < x_off+70
{
	if player.y < room_height/2
	{
		move = "top_left"
	}else move = "bottom_left"
}
if player.x >  x_off+410-70
{
	if player.y < room_height/2
	{
		move = "top_right"
	}else move = "bottom_right"
}
if player.y < y_off+70
{
	if player.x < room_width/2
	{
		move = "top_left"
	}else move = "top_right"
}
if player.y > y_off+410-70
{
	if player.x < room_width/2
	{
		move = "bottom_left"
	}else move = "bottom_right"
}else move = "shockwave"

with(enemy){event_user(2);};