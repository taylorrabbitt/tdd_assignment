import java.util.Scanner;

public class Problem2 {
    //Assumption: the input is integer, pi = 3

    //a for square length, circle radius,and rectangle length
    //b for square breadth
    public static String AreaandPeri(String input,int a, int b) {
        Scanner sc = new Scanner(System.in);
        //System.out.println("Choose a shape: (C)ircle or (R)ectangle or (S)quare");
        //String input = sc.nextLine();
        String result;
        if(input.equals("C") || input.equals("S") || input.equals("R")){
            int area = 0;
            int perimeter = 0;
            if(input.equals("C")){
                //System.out.println("Circle Radius");
                //double r = Integer.parseInt(sc.nextLine());
                area = 3 * a * a;
                perimeter = 2 * 3 * a;
            }else if(input.equals("S")){
                //System.out.println("Square Length");
                //double s = Integer.parseInt(sc.nextLine());
                area = a * a;
                perimeter = 4*a;
            }else{
                //System.out.println("Rectangle Length");
                //double length = Integer.parseInt(sc.nextLine());
                //System.out.println("Rectangle Breadth");
                //double breadth = Integer.parseInt(sc.nextLine());
                area = a * b;
                perimeter = 2*(a + b);
            }
            //System.out.println("Area: "+area+" square units and Perimeter: "+perimeter+" units");
            result = "Area: "+area+" square units and Perimeter: "+perimeter+" units";
        }else{
            //System.out.println("invalid input");
            result = "invalid input";
        }

        return result;
    }

    public static void test(String input,int a, int b, String expect){
        String output=AreaandPeri(input,a,b);
        if(expect.equals(output)){
            System.out.println("Test passed!");
        }else{
            System.out.println("Test failed");
            System.out.println("Output: " + output);
            System.out.println("Expected: "+expect);
        }

    }

    public static void main(String[] args) {
        //test 1
        String expected = "Area: 20 square units and Perimeter: 18 units";
        test("R",4,5,expected);

        //test 2
        expected = "Area: 12 square units and Perimeter: 12 units";
        test("C",2,0,expected);

        //test 3
        expected = "Area: 9 square units and Perimeter: 12 units";
        test("S",3,0,expected);

        //test 4
        expected = "invalid input";
        test("A",2,0,expected);

        //test 5
        expected = "Area: 0 square units and Perimeter: 0 units";
        test("R",0,0,expected);
        
    }
}
