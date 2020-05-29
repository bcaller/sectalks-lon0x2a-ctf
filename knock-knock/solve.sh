# This one was supposed to work but only occasionally succeeded
knock -v sectalks-ctf.caller.xyz 107 110 111 99:udp 75; nc sectalks-ctf.caller.xyz 61217

# This one actually works
echo -e "107\n110\n111" | xargs -I{} timeout 1s nc sectalks-ctf.caller.xyz {}
echo hi | timeout 1s nc sectalks-ctf.caller.xyz -u 99
timeout 1s nc sectalks-ctf.caller.xyz 75
timeout 1s nc sectalks-ctf.caller.xyz 61217
