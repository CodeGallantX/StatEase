import streamlit as st
import time

# Initial setup
bus = [] 
stand_queue = ['Mr Paul', 'Miss Jane', 'John']
sit_queue = ['Pa Okonkwo', 'Bode', 'Sister Jennifer', 'Usman', 'Emeka', 'Zainab', 'Joshua', 'Ilerika', 'Ekukeu', 'Prof. Johnson', 'Iyalode', 'Rish kid', 'Alagba']

balance = {
    'user': 100  # Default user balance
}

# Function to board the bus
def board(person):
    fare = 250
    if person not in balance:
        st.warning(f"{person} is not registered. Please top-up your Cowry Card!")
        return False

    if balance[person] >= fare:
        balance[person] -= fare
        bus.append(person)
        st.success(f"{person}, you have successfully boarded the bus!")
        st.write(f"Remaining balance: ₦{balance[person]}")
        return True
    else:
        st.error(f"{person}, insufficient balance to board the bus!")
        st.warning("Please top-up your Cowry Card.")
        return False

# Function to top-up Cowry Card
def cowrycard_topup(person):
    if person not in balance:
        balance[person] = 0  # Initialize balance for new user
    
    topup_amount = st.number_input(f"Enter top-up amount for {person}:", min_value=0, step=50)
    if st.button(f"Top-up {person}'s Card"):
        balance[person] += topup_amount
        st.success(f"₦{topup_amount} successfully added to {person}'s Cowry Card!")
        st.write(f"New balance: ₦{balance[person]}")

# Function to handle queue
def queue(person):
    st.write("Queues:")
    st.write(f"1. Standing Queue: {len(stand_queue)} people")
    st.write(f"2. Sitting Queue: {len(sit_queue)} people")

    choice = st.radio("Choose your queue:", ["Sitting Queue", "Standing Queue"])
    if choice == "Sitting Queue":
        if len(sit_queue) < 10:
            sit_queue.append(person)
            st.success(f"{person} joined the Sitting Queue!")
        else:
            st.warning("Sitting Queue is full. Please join the Standing Queue.")
    elif choice == "Standing Queue":
        stand_queue.append(person)
        st.success(f"{person} joined the Standing Queue!")

# Function to simulate bus movement
def bus_moving():
    st.info("🚌 The bus is now moving!")
    progress_text = "Bus Progress"
    for progress in range(0, 101, 25):
        st.progress(progress, text=progress_text)
        time.sleep(2)
    st.success("Bus has arrived at the final destination!")
    st.balloons()

# Main function
def main():
    st.title("LAMATA BRT Bus Simulator")

    person = st.text_input("Enter your name to start:")
    if person:
        if person not in balance:
            balance[person] = 100  # Initialize new user's balance
            st.info(f"{person} registered with an initial balance of ₦100.")
        
        st.write(f"Welcome, {person}!")
        options = st.radio(
            "Choose an action:",
            ['Join Queue', 'Check Balance', 'Top-up Card', 'Quit']
        )

        if options == 'Join Queue':
            queue(person)
            if board(person):
                bus_moving()
        elif options == 'Check Balance':
            st.subheader(f"Your balance: ₦{balance[person]}")
        elif options == 'Top-up Card':
            cowrycard_topup(person)
        elif options == 'Quit':
            st.write("Thank you for using the LAMATA BRT Bus Simulator. Goodbye!")
            st.stop()

# Run the application
if __name__ == '__main__':
    main()
