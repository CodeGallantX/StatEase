import streamlit as st
# LAMATA BRT  BUS
import time

bus = [] 
stand_queue = ['Mr Paul', 'Miss Jane', 'John']
sit_queue = ['Pa Okonkwo', 'Bode', 'Sister Jennifer', 'Usman', 'Emeka', 'Zainab', 'Joshua', 'Ilerika', 'Ekukeu', 'Prof. Johnson', 'Iyalode', 'Rish kid', 'Alagba']

balance = {
    'name': 100
}

# Board Bus function
def board(person):
    if person in balance:
        while stand_queue.count(person) < 0:
            fare = 250
            break
        
        if balance['name'] >= fare:
            balance['name'] - fare == balance
            # bus.append(person) 
            st.write("Ikorodu Terminal (Ikorodu - Oshodi)")
            return True       
        else:
            st.write(f"{person}, sorry you cannot board this bus. Your money is short")
            st.warning(f"Owo yin o pe!")
            cowrycard_topup(balance)
            return False
        
        
def cowrycard_topup(balance):
    st.write("Top-up ya card!! We no dey collect waso ooh!")
    while True:
        price = st.number_input("How much do you want to buy into your card? ")
        if price > 0:
            st.success(f"You have successfully loaded ₦{price}")
            break  
        else:
            st.warning("Abeg no waste my time ooh! Wetin you wan do for here sef?")
            continue
    balance.append(price)

def queue(person):       
    st.write("1. Standing queue: ", len(stand_queue), ' \n> Waiting time: ', len(stand_queue), 'seconds')
    st.write("2. Sitting queue: ", len(sit_queue), '\n> Waiting time: ', len(sit_queue), 'seconds')

    choice = st.radio("Select queue to enter:",
             ["Sitting Queue", "Standing Queue"],
             index=None
             )
    if choice == 'Sitting Queue':
        st.info("Standing queue joined.")
        with st.spinner("Seats full! Enter in with your Cowry cards to stand in bus."):
            time.sleep(len(stand_queue))
        st.info(f"{person} tap in your card to enter.")
        st.write(balance['name'])
        
    elif choice == '2':
        st.info("Standing Queue joined.")
        with st.spinner("Bus well parked! Enter in with your Cowry cards to seat in bus"):
            time.sleep(len(sit_queue))
        st.info(f"{person} tap-in your card to enter.")
        st.write(balance['name'])
    else:
        st.warning("You no wan enter queue? No chance me ooh!!")
        with st.spinner("You no go enter bus. Comot for road, make i enter jare.."):
            time.sleep(2)

def bus_moving():
    progress_text = "...🚌 The bus in on the move..."
    st.progress(25, progress_text)
    time.sleep(3)
    with st.spinner("Mile 12 wa ooh!"):
        time.sleep(3)
        st.write("(brakes screech) 🚌 The bus stopped.")
        st.write("On bole ooh!")
        time.sleep(2)
        st.progress(56,  progress_text)
        st.write('Ojota wa ooh! On bole ooh...')
        st.progress(84, progress_text)
        time.sleep(2)
        st.progress(84, progress_text)
        st.progress(100, progress_text)
        st.success("...........Arrived at final destination............")
        st.balloons()
        st.progress(100, progress_text)
        st.info('All passengers, please alight gently from the bus')


def main():
    st.subheader("BRT Boarding Transport Simulator")
    person = st.text_input("Enter name to start: ")
    # balance['name'] = person
    time.sleep(3)

    options = st.radio(
        "What would you like to do?",
        ['Join queue', 'Check balance', 'Top-up your card', "Quit"],
        index=1
        # captions
    )

    if options == 'Join queue':
        queue(person)
        board(person)
        bus_moving()
    elif options == 'Check balance':
        st.subheader(f'Your balance is {balance['name']}')

    elif options == 'Top-up your card':
        cowrycard_topup(balance)
    elif options == 'Quit':
        st.write("Come back anytime.")
        with st.spinner("Exiting application....."):
            time.sleep(3)
        st.success("Application Exited!")
    else:
        st.warning("Invalid choice! choose again.")

# Execution of main function
if __name__ == '__main__':
    main()