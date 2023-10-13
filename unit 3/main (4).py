package myFirstJavaProject;
import java.util.Scanner;
public class myFirstJavaProgram;
{

	public static void main(String args[]) {

		// Variable Initialization
		String strSuccess = "Bravo!! Now you are a Java programmer";
		String strFailure = "Unfortunately You are not successfull right now, but trust me You will :)";

		System.out.println("Let's understand Java program step by step");
		System.out.println("So, are you ready for it? Please type Yes or No");
		Scanner answer = new Scanner(System.in);
		String input = answer.nextLine();
		
		if (input.equals("Yes")) {
			System.out.println(strSuccess);
		} else {
			System.out.println(strFailure);
		}
}