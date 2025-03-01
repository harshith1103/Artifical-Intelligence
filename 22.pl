% Facts: Birds that cannot fly
flightless(ostrich).
flightless(penguin).
flightless(kiwi).
flightless(emperor_penguin).  % Another flightless bird
flightless(raptor).            % Another flightless bird

% Facts: Birds that can fly
can_fly(sparrow).             % A bird that can fly
can_fly(eagle).               % Another bird that can fly
can_fly(hummingbird).         % Another bird that can fly
can_fly(falcon).              % Another bird that can fly

% Rule: A bird can fly unless it is flightless
can_fly(Bird) :- \+ flightless(Bird).

% Rule: A bird cannot fly if it is in the flightless list
cannot_fly(Bird) :- flightless(Bird).

% To check if a bird can fly or cannot fly
check_flight(Bird) :-
    (can_fly(Bird) -> 
        format('~w can fly.~n', [Bird]) 
    ; 
        format('~w cannot fly.~n', [Bird])
    ).