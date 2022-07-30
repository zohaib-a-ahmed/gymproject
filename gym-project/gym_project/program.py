
class Program:

    def __init__(self, age, gender, days, hours, targets, bodytype):

        self.gender = gender # 0 or 1, male/female

        if(hours <= 1.5): # denote short/long workout
            self.time = 0 # short
        else:
            self.time = 1 # long

        self.targets = targets # List of target areas; 0:Arms, 1:Chest, 2:Shoulders, 3:Back, 4:Glutes, 5:Legs

        self.bodytype = bodytype # 1:Skinny/Lean, 2:Skinny/Fat, 3:Overweight, 4:Semi-Muscular
        # To incorporate cardio or not

        if(age > 30):
            self.freeweight = False
        else:
            self.freeweight = True

        self.workout = {}

        if(days < 3): # determine split
            self.full_body_split()
        else:
            self.rotation()

        self.print_workout()


    def full_body_split(self):
        # Returns string of correct format / output
        type = self.type_of_workout(False)
        
        self.workout["Daily Routine"] = " "
        self.chest(type)
        self.shoulders(type)
        self.back(type)
        self.triceps(type)
        self.biceps(type)
        self.legs(type)
        
    def rotation(self):
        # returns string of correct format / output
        type = self.type_of_workout(True)
        
        self.workout["Rotational"] = " "
        self.workout["Push Day"] = " "
        self.chest(type)
        self.shoulders(type)
        self.triceps(type)
        self.workout["Pull Day"] = " "
        self.back(type)
        self.biceps(type)
        self.workout["Leg Day"] = " "
        self.legs(type)


    def type_of_workout(self, split):
        # Split information type into 8 categories to define workouts

        if split: # Rotational Split
            if(self.gender == 0): # Male
                if self.freeweight: # Free Weight Use
                    if self.time == 0: # Short Workout
                        return 1
                    else:
                        return 2 # Long Workout
                else:
                    if self.time == 0:
                        return 3
                    else:
                        return 4
            else: # Female
                if self.freeweight:
                    if self.time == 0:
                        return 5
                    else:
                        return 6
                else:
                    if self.time == 0:
                        return 7
                    else:
                        return 8
        else: # Full Body Split
            if(self.gender == 0): # Male
                if self.freeweight: # Free Weight Use
                    return 1
                else:
                    return 3
            else: # Female
                if self.freeweight:
                    return 5
                else:
                    return 7
 
    def chest(self, type):

        if(type ==  1):
            self.workout["Incline Dumbbell Press"] = " 4x8"
        elif(type ==  2):
            self.workout["Bench Press"] = " 4x10/8/6/4"
            self.workout["Incline Dumbbell Press"] = " 4x8"
        elif(type == 5):
            self.workout["Dumbbell Press"] = " 3x8"
        elif(type == 6):
            self.workout["Dumbbell Press"] = " 3x8"
            self.workout["Incline Dumbbell Press"] = " 3x8"
        else:
            self.workout["Chest Press Machine"] = " 3x10"

        if(self.targets[1] == 1):
            self.workout["Chest Focused Dips"] = " 3xTo-Failure"
        
    def back(self, type):

        if(type ==  1):
            self.workout["Barbell Back Rows"] = " 4x8"
            self.workout["Lat Pulldowns"] = " 3x12"
        elif(type ==  2):
            self.workout["Barbell Back Rows"] = " 4x8"
            self.workout["Lat Pulldowns"] = " 3x12"
            self.workout["Pull Ups"] = " 3xTo-Failure"
        elif(type == 5):
            self.workout["Cable Back Row"] = " 3x8"
        elif(type == 6):
            self.workout["Cable Back Row"] = " 3x8"
            self.workout["Lat Pulldown"] = " 3x8"
        elif((type == 4) or (type == 8)):
            self.workout["Machine Back Row"] = " 3x10"
            self.workout["Machine Lat Pulldown"] = " 3x10"
        else:
            self.workout["Machine Back Row"] = " 3x10"

        if(self.targets[3] == 1):
            self.workout["Cable Lat Pushdowns"] = " 3x10"

    def shoulders(self, type):

        if((type ==  1) or (type == 2)):
            self.workout["Dumbbell Lateral Raises"] = " 4x12"
        elif(type == 5):
            self.workout["Dumbbell Shoulder Press"] = " 3x8"
        elif(type == 6):
            self.workout["Dumbbell Shoulder Press"] = " 3x8"
            self.workout["Dumbbell Lateral Raises"] = " 4x12"
        else:
            self.workout["Machine Shoulder Press"] = " 3x8"
        
        if(self.targets[2] == 1):
            self.workout["Cable Lateral Raises"] = " 3x12"

    def biceps(self, type):

        if(type ==  1):
            self.workout["Hammer Curls"] = " 3x10"
            self.workout["Cable Bar Curls"] = " 3x10"
        elif(type ==  2):
            self.workout["Hammer Curls"] = " 3x10"
            self.workout["EZ Bar Curls"] = " 3x10"
            self.workout["Cable Bar Curls"] = " 3x12"
        elif(type == 5):
            self.workout["Hammer Curls"] = " 3x10"
        elif(type == 6):
            self.workout["Hammer Curls"] = " 3x10"
            self.workout["Dumbbell Curls"] = " 3x10"
        elif((type == 4) or (type == 8)):
            self.workout["Dumbbell Curls"] = " 3x8"
            self.workout["Cable Bar Curls"] = " 3x8"
        else:
            self.workout["Dumbbell Curls"] = " 3x10"
        
        if(self.targets[0] == 1):
            self.workout["Preacher Curl Machine"] = " 3x10"

    def triceps(self, type):

        if(type ==  1):
            self.workout["Tricep Overhead Extensions"] = " 3x12"
            self.workout["Tricep Rope Pushdowns"] = " 3x10"
        elif(type ==  2):
            self.workout["Tricep Overhead Extensions"] = " 3x12"
            self.workout["Tricep Rope Pushdowns"] = " 3x10"
            self.workout["Single Arm Bent-Over Tricep Extensions"] = " 3x10"
        elif(type == 6):
            self.workout["Tricep Pushdowns"] = " 3x12"
            self.workout["Tricep Rope Pushdowns"] = " 3x10"
        else:
            self.workout["Tricep Pushdowns"] = " 3x10"
        
        if(self.targets[0] == 1):
            self.workout["Skullcrusher Tricep Extensions"] = " 3x12"

    def legs(self, type):

        if(type ==  1):
            self.workout["Hack Squat"] = " 5x8"
            self.workout["Hamstring Curls"] = " 3x15"
            self.workout["Calf Raises"] = " 4x15"
            self.workout["Quad Extensions"] = " 3x12"
        elif(type ==  2):
            self.workout["Barbell Back Squat"] = " 4x12/10/8/10"
            self.workout["Bulgarian Single Leg Split Squat"] = " 3x12"
            self.workout["Leg Press"] = " 3x20"
            self.workout["Hamstring Curls"] = " 3x15"
            self.workout["Calf Raises"] = " 4x15"
            self.workout["Quad Extensions"] = " 3x12"
        elif(type == 5):
            self.workout["Barbell Back Squat"] = " 4x10/8/8/10"
            self.workout["Hip Thrusts"] = " 4x12"
            self.workout["Hamstring Curls"] = " 3x15"
            self.workout["Calf Raises"] = " 4x15"
            self.workout["Quad Extensions"] = " 3x12"
        elif(type == 6):
            self.workout["Barbell Back Squat"] = " 4x10/8/8/10"
            self.workout["Hip Thrusts"] = " 4x12"
            self.workout["Bulgarian Single Leg Split Squat"] = " 3x12"
            self.workout["Leg Press"] = " 3x20"
            self.workout["Hamstring Curls"] = " 3x15"
            self.workout["Calf Raises"] = " 4x15"
            self.workout["Quad Extensions"] = " 3x12"
        else:
            self.workout["Leg Press Machine"] = " 4x12"
            self.workout["Seated Quad Extension"] = " 3x10"
            self.workout["Seated Hamstring Curl"] = " 3x10"
        
        if((self.targets[4] == 1) or (self.targets[5] == 1)):
            self.workout["Goblet Squats"] = " 3x15"
        
    def print_workout(self):
        print(self.workout)
    
