/// @description Generall attacking logic (after move has been set, either by "AI" or randomly)

switch move
{
	case "shockwave":
		instance_create_layer(x, y, "shadows", attack_shadow_middle) //initialize the shadow for attack to run attack
	break;
	case "bottom_left":
		instance_create_layer(x, y, "shadows", attack_bottom_left) //initialize the shadow for attack to run attack
	break;
	case "bottom_right":
		instance_create_layer(x, y, "shadows", attack_bottom_right) //initialize the shadow for attack to run attack
	break;
	case "top_left":
		instance_create_layer(x, y, "shadows", attack_top_left) //initialize the shadow for attack to run attack
	break;
	case "top_right":
		instance_create_layer(x, y, "shadows", attack_top_right) //initialize the shadow for attack to run attack
	break;
}