!------------------------------------------------
! Ezra S. Brooker
!
! https://www.reddit.com/r/dailyprogrammer/comments/n94io8/20210510_challenge_389_easy_the_monty_hall_problem/
!
! For the purpose of today's challenge, the Monty Hall scenario goes like this:
!
! There are three closed doors, labeled #1, #2, and #3. Monty Hall randomly selects 
! one of the three doors and puts a prize behind it. The other two doors hide nothing.
!
! A contestant, who does not know where the prize is, selects one of the three doors. 
! This door is not opened yet.
!
! Monty chooses one of the three doors and opens it. The door that Monty opens 
! (a) does not hide the prize, and (b) is not the door that the contestant selected. 
! There may be one or two such doors. If there are two, Monty randomly selects one or 
! the other.
!
! There are now two closed doors, the one the contestant selected in step 2, and one 
! they didn't select. The contestant decides whether to keep their original choice, or 
! to switch to the other closed door.
!
! The contestant wins if the door they selected in step 4 is the same as the one Monty 
! put a prize behind in step 1.
!
! Challenge
! A contestant's strategy is given by their choices in steps 2 and 4. Write a program 
! to determine the success rate of a contestant's strategy by simulating the game 1000 
! times and calculating the fraction of the times the contestant wins. Determine the 
! success rate for these two contestants:
!
! Alice chooses door #1 in step 2, and always sticks with door #1 in step 4.
!
! Bob chooses door #1 in step 2, and always switches to the other closed door in step 4.
!
! Optional bonus
! Find success rates for these other contestants:
!
! Carol chooses randomly from the available options in both step 2 and step 4.
!
! Dave chooses randomly in step 2, and always sticks with his door in step 4.
!
! Erin chooses randomly in step 2, and always switches in step 4.
!
! Frank chooses door #1 in step 2, and switches to door #2 if available in step 4. 
! If door #2 is not available because it was opened, then he stays with door #1.
!
! Gina always uses either Alice's or Bob's strategy. She remembers whether her previous 
! strategy worked and changes it accordingly. On her first game, she uses Alice's strategy. 
! Thereafter, if she won the previous game, then she sticks with the same strategy as the 
! previous game. If she lost the previous game, then she switches (Alice to Bob or Bob to Alice).
!
! It's possible to calculate all of these probabilities without doing any simulation, of 
! course, but today's challenge is to find the fractions through simulation.
!
! (This is a repost of Challenge #49 [easy], originally posted by u/oskar_s in May 2012.)
!
!------------------------------------------------
program montyhall
implicit none
    integer, parameter :: num_trials = 100000
    integer, parameter :: num_doors = 3
    integer, parameter :: seed=54785
    real(kind=8)       :: winrat, rando_calrissian
    integer            :: i, j, winner, choice, closed, won, temp
    character(len=5)   :: player(7)
    logical            :: bob_strat

    call srand(seed)

    player = ["Alice", "Bob  ", "Carol", "Dave ", "Erin ", "Frank", "Gina "]

    !! Player loop    
    do j = 1, 7
        
        bob_strat = .false.
        won = 0

        !! Simulation loop
        do i = 1,num_trials
            
            !! Select the winning door
            call random_number(rando_calrissian)
            winner = 1 + floor((num_doors)*rando_calrissian)
            
            !! Player makes first choice
            choice = 1
            if ( j == 3 .or. j == 4 .or. j == 5 ) then
                !! Carol, Dave, and Erin
                call random_number(rando_calrissian)
                choice = 1 + floor((num_doors)*rando_calrissian)
            end if

            !! Discard junk doors
            closed = winner
            if (choice == winner) then
                do while (closed == winner)
                    call random_number(rando_calrissian)
                    closed = 1 + floor((num_doors)*rando_calrissian)
                enddo
            endif
            
            !! Player makes second choice
            if ( j == 2 .or. j == 5 ) then
                !! Bob and Erin
                choice = closed
            elseif ( player(j) == "Carol" ) then
                temp = 0
                do while (temp /= choice .and. temp /= closed)
                    call random_number(rando_calrissian)
                    temp = 1 + floor((num_doors)*rando_calrissian)
                end do
                choice = temp
            elseif ( j == 6 .and. closed == 2 ) then
                !! Frank
                choice = closed
            elseif ( j == 7 .and. bob_strat ) then
                !! Gina using Bob's strategy
                choice = closed
            endif

            !! Update win total if possible
            if (choice == winner) then
                won = won + 1
            elseif ( j == 7 ) then
                if (bob_strat) then
                    bob_strat = .false.
                else
                    bob_strat = .true.
                endif
            endif
        enddo
        
        winrat = real(won, kind=8)/real(i, kind=8)
        write(*,"(a5,a,F0.4,a)") player(j), " win percentage: ", 100*winrat,"%"
    enddo 

end program montyhall
