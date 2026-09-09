class HelloWorld:
    def __init__(self):
        """Initialize the HelloWorld instance."""
        self.running = True
    
    def start(self):
        """Start the HelloWorld instance."""
        print("HelloWorld instance started!")
        self.draw_frog()
        self.run()
    
    def draw_frog(self):
        """Draw a cute ASCII frog."""
        frog = """
          _~
      ___( o>
      / (  /
     /   (___/
    (____/
        """
        print(frog)
    
    def run(self):
        """Run the main loop of the HelloWorld instance."""
        while self.running:
            try:
                user_input = input("Enter a command (or 'quit' to exit): ").strip()
                
                if user_input.lower() == "quit":
                    self.stop()
                else:
                    print(f"Received: {user_input}")
            except KeyboardInterrupt:
                self.stop()
    
    def stop(self):
        """Stop the HelloWorld instance."""
        self.running = False
        print("HelloWorld instance stopped!")


if __name__ == "__main__":
    while True:
        user_input = input("Enter 'Hello World' to start: ").strip()
        
        if user_input == "Hello World":
            instance = HelloWorld()
            instance.start()
            break
        else:
            print("Please enter 'Hello World' to start.")
