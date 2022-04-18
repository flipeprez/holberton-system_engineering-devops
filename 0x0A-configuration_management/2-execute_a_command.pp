#excecute a command 
exec { 'pkill killmenow':
    command => 'killmenow',
}
