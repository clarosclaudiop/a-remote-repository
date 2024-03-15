# Yei2
# Yei3
# Yei5
# Yei4
# Yei6
# Yei7
# Yei8
# Changing one line at one file, has the effect: 1 insertion(+), 1 deletion(-), 1 file changes
# SIETE
# Commits are copied into the local git repository after fetch? Or not really, and merge does that.
    # Pues git fetch sí descarga todos commits que no tenías del repositorio remoto, de una forma tal que aparecen al hacer git log --all --oneline --graph.
    # Es decir, esas commits del remoto sí quedan dentro del repositorio luego de fetch.    
    # Mira, esto aparece:
    #* dce5a31 (origin/main) Se agregó una question con esta commit.
    #* c1d4853 (HEAD -> main) Se renombró newfile.py to oldfile.py.
    # Merge fusiona branches, es decir, las commits apuntadas.
