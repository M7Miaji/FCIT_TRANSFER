class require():
    def First(CPIT, CPCS):
        if CPIT >= 80:
            if CPCS >= 75:
                return True
        return False

    def Second(MATH, CPCS):
        if MATH >= 85:
            if CPCS >= 75:
                return True
        return False

    def Third(ELI, CPCS_CPIT):
        if ELI >= 85:
            if CPCS_CPIT >= 80:
                return True
        return False

    def Fourth(average):
        if average >= 3.75:
                return True
        return False



