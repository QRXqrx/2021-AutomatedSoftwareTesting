public class BankAccount {
	
	private int balance;
	private int numberOfWithdrawals;


	public BankAccount(int amount){
		balance = amount;
	}

	public void deposit(int amount){
		if (amount>0)
			System.out.println("I am easily reachable in deposit");
			balance = balance + amount;
	}

	public void withdraw(int amount){
		if(amount>balance){
			System.out.println("I am easily reachable in withdraw");
			return;
		}
		if (numberOfWithdrawals>=5){// was 10
			assert(false);
			System.out.println("I am very hard to reach in withdraw");
			return;
		}
		balance = balance - amount;
		numberOfWithdrawals++;
	}

	/* ----- Test Driver ----- */

	public static void testDriver(int length){
		BankAccount b = new BankAccount(0);
		for (int i=0; i<length; i++){
			switch(flag(true)) {
				case 0:
					b.deposit(10);
					break;
				case 1:
					b.withdraw(1);
					break;
			}
		}
	}

	public static int flag(boolean x) {
	if (x)
		return 1;
	else
		return 0;
	}

	public static void main(String[] args){
		testDriver(3);
		System.out.println();
	}
}
