step = step + 1

if step > 50
{
	image_index = 1
}
if step >= 80
{
	image_index = 2
}
if step >= 110
{
	visible = false
	instance_create_layer(x, y, "attacks", attack_middle)
}
if step >= 150
{
	instance_destroy(self)
	with(attack_middle){event_user(0);};
}
