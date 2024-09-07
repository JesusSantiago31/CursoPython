flag_register = 0x1234
# Representacion:
#flag_register = 0000000000000000000000000000x000

#Reiniciar tu bit
flag_register = flag_register & ~the_mask
flag_register &= ~the_mask

#Establece tu bit
flag_register = flag_register | the_mask
flag_register |= the_mask

#Niega tu bit
flag_register = flag_register ^ the_mask
flag_register ^= the_mask




