
class Program:

    def __init__(self, age, gender, days, hours, targets, bodytype):

        self.gender = gender # 0 or 1, male/female

        if(hours <= 1): # denote short/long workout
            self.time = 0 # short
        else:
            self.time = 1 # long

        self.targets = targets # List of target areas; 0:Arms, 1:Chest, 2:Shoulders, 3:Core, 4:Glutes, 5:Legs

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

    def full_body_split(self):
        # Returns string of correct format / output
        split = False
        pass

    def rotation(self):
        # returns string of correct format / output
        split = True
        pass

    def type_of_workout(self, split):
        # Split information type into 8 categories to define workouts

        if split: # Rotational Split
            if self.gender == 0: # Male
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

    def chest(self, split):
        type = self.type_of_workout(split)

        if(type ==  1):
            self.workout["Incline Dumbbell Press"] = "4x8"
        elif(type ==  2):
            self.workout["Bench Press"] = "4x10/8/6/4"
            self.workout["Incline Dumbbell Press"] = "4x8"
        elif(type == 5):
            self.workout["Dumbbell Press"] = "3x8"
        elif(type == 6):
            self.workout["Dumbbell Press"] = "3x8"
            self.workout["Incline Dumbbell Press"] = "3x8"
        else:
            self.workout["Chest Press Machine"] = "3x10"
        
    def back(self, split):
        if(type ==  1):
            self.workout["Barbell Back Rows"] = "4x8"
            self.workout["Lat Pulldowns"] = "3x12"
        elif(type ==  2):
            self.workout["Barbell Back Rows"] = "4x8"
            self.workout["Lat Pulldowns"] = "3x12"
            self.workout["Pull Ups"] = "3xTo-Failure"
        elif(type == 5):
            self.workout["Cable Back Row"] = "3x8"
        elif(type == 6):
            self.workout["Cable Back Row"] = "3x8"
            self.workout["Lat Pulldown"] = "3x8"
        elif((type == 4) or (type == 8)):
            self.workout["Machine Back Row"] = "3x10"
            self.workout["Machine Lat Pulldown"] = "3x10"
        else:
            self.workout["Machine Back Row"] = "3x10"

    def shoulders(self, split):
        if((type ==  1) or (type == 2)):
            self.workout["Lateral Raises"] = "4x12"
        elif(type == 5):
            self.workout["Dumbbell Shoulder Press"] = "3x8"
        elif(type == 6):
            self.workout["Dumbbell Shoulder Press"] = "3x8"
            self.workout["Lateral Raises"] = "4x12"
        else:
            self.workout["Machine Shoulder Press"] = "3x8"

    def biceps(self, split):
        if(type ==  1):
            self.workout["Hammer Curls"] = "3x10"
            self.workout["Cable Bar Curls"] = "3x10"
        elif(type ==  2):
            self.workout["Hammer Curls"] = "3x10"
            self.workout["EZ Bar Curls"] = "3x10"
            self.workout["Cable Bar Curls"] = "3x12"
        elif(type == 5):
            self.workout["Hammer Curls"] = "3x10"
        elif(type == 6):
            self.workout["Hammer Curls"] = "3x10"
            self.workout["Dumbbell Curls"] = "3x10"
        elif((type == 4) or (type == 8)):
            self.workout["Dumbbell Curls"] = "3x8"
            self.workout["Cable Bar Curls"] = "3x8"
        else:
            self.workout["Dumbbell Curls"] = "3x10"

    def triceps(self, split):
        if(type ==  1):
            self.workout["Tricep Overhead Extensions"] = "3x12"
            self.workout["Tricep Rope Pushdowns"] = "3x10"
        elif(type ==  2):
            self.workout["Tricep Overhead Extensions"] = "3x12"
            self.workout["Tricep Rope Pushdowns"] = "3x10"
            self.workout["Single Arm Bent-Over Tricep Extensions"] = "3x10"
        elif(type == 6):
            self.workout["Tricep Pushdowns"] = "3x12"
            self.workout["Tricep Rope Pushdowns"] = "3x10"
        else:
            self.workout["Tricep Pushdowns"] = "3x10"

    def legs(self, split):
        if(type ==  1):
            self.workout["Hack Squat"] = "5x8"
            self.workout["Hamstring Curls"] = "3x15"
            self.workout["Calf Raises"] = "4x15"
            self.workout["Quad Extensions"] = "3x12"
        elif(type ==  2):
            self.workout["Barbell Back Squat"] = "4x12/10/8/10"
            self.workout["Bulgarian Single Leg Split Squat"] = "3x12"
            self.workout["Leg Press"] = "3x20"
            self.workout["Hamstring Curls"] = "3x15"
            self.workout["Calf Raises"] = "4x15"
            self.workout["Quad Extensions"] = "3x12"
        elif(type == 5):
            self.workout["Barbell Back Squat"] = "4x10/8/8/10"
            self.workout["Hip Thrusts"] = "4x12"
            self.workout["Hamstring Curls"] = "3x15"
            self.workout["Calf Raises"] = "4x15"
            self.workout["Quad Extensions"] = "3x12"
        elif(type == 6):
            self.workout["Barbell Back Squat"] = "4x10/8/8/10"
            self.workout["Hip Thrusts"] = "4x12"
            self.workout["Bulgarian Single Leg Split Squat"] = "3x12"
            self.workout["Leg Press"] = "3x20"
            self.workout["Hamstring Curls"] = "3x15"
            self.workout["Calf Raises"] = "4x15"
            self.workout["Quad Extensions"] = "3x12"
        else:
            self.workout["Leg Press Machine"] = "4x12"
            self.workout["Seated Quad Extension"] = "3x10"
            self.workout["Seated Hamstring Curl"] = "3x10"
    
    def printWorkout(self):
        for key, value in self.workout.items():
            print(key + value)

#if __name__ == '__main__':
    #butt = Program(22, 0, 5, )