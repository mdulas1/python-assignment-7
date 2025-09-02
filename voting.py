"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""

candidates = {}
voters = set()

def register_candidates(*args, **kwargs):
    """Register candidates with optional metadata.
    """
    for name in args:
        if name not in candidates:
            candidates[name] = {"votes": 0}
            # Add optional metadata like party, region
            for key, value in kwargs.items():
                candidates[name][key] = value
        else:
            print(f"Candidate {name} already registered!")


def cast_vote(voter_id, candidate):
    """Cast vote if voter has not voted before.
        after all the vote logic is completeted sucessfully,
        return: Vote casted for {candidate}.
    """
    if voter_id in voters:
        return f"Voter {voter_id} has already voted!"
    
    if candidate not in candidates:
        return f"Candidate {candidate} not found!"
    
    # Record vote
    voters.add(voter_id)
    candidates[candidate]["votes"] += 1
    
    return f"Vote casted for {candidate}."


def election_result():
    """Return the winner(s)."""
    # max_votes = #add logic
    # winners = #add logic
    # return {"winners": winners, "candidates": candidates}

    if not candidates:
        return {"winners": [], "candidates": candidates}
    
    # Find max votes
    max_votes = max(c["votes"] for c in candidates.values())
    winners = [name for name, data in candidates.items() if data["votes"] == max_votes]
    
    return {"winners": winners, "candidates": candidates}

register_candidates("victor","Aisha",party="PDP",region="North")
register_candidates("musa","john",party="APC",region="South")

print(cast_vote("v001","victor"))
print(cast_vote("v002",'musa'))
print(cast_vote("v001","Aisha"))
print(cast_vote("v003","Aisha"))

print(election_result())
