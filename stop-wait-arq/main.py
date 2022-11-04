def algo(sliding_size, frames):
    """
    Args :
     sliding_size (integer) --  The size of the sliding window
     frames (list) --  The number of frames to be sent 

    Returns :
        status (1) -- Acknowledgement status of the frames that are being sent
    """
    status = ""
    for fr in range(1, len(frames)):
        if fr % sliding_size == 0 :
            status += "\nThe acknowledgment of the frame {}  has been received  by the sender is \n".format(frames[fr])
        else :
            status += "\n{}  :: frame\n".format(frames[fr])
    if len(frames) % sliding_size != 0:
        status += "\nThe acknowledgment of the frame {} has been received by the sender is \n".format(frames[fr])
    
    return status;


if __name__ == '__main__':
    
    print("\n\nEnter the size of the sliding window and the nos frames that you want to enter ::")
    size,frame_sz = [int(a) for a in input("Enter the values separated by the commas :: ").split(",")]
    
    print("\n\nEnter the values for the frames now for {} nos of times ".format(frame_sz))
    frames = input("Enter the values for the list separated by the space ::: ").split(",")

    result = algo(size, frames)
    print(result)
        

