import openai
openai.api_key = "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"

import openai

def summarize_article(article_text):
    prompt = f"Please summarize the following article:\n{article_text}\nSummary:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,  # Adjust this value based on the desired summary length.
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1,
    )

    summary = response.choices[0].text.strip()
    return summary


txt = '''For us to join as you are a very useful I Solution Architect team. So he's just coming in his Yeah, so that's fine. We can continue and when the from production support wins and from service management

okay. So yeah, so the the thing I believe that you have, I don't need to really go through the the agenda, right. So the key, responsibility and objective is to make sure that the architecture and the design being compliant right and aligned with the blueprint of just paying and also aligned in terms of the technical expectation on the scope, right. So, the one very important aspect is a security aspect. perspective. We don't want to have any things implemented and later we are being hammered that does not align with the security policy. Review the operational requirements. So in this unnamed dispute, or things that we cannot agree on, right, we also make use of this form to agree on the disagreement.

Yeah, one point could also whatever we are designing for clinics, we are discussing with you what are what are the what are the changes we are going to do it right for finish application as soon as the internal applications right so we discuss with you so do we need to do any new additional information to you or something something?

Oh, yeah. Yeah, so thank you. So we understand that, but just one some not really a problem, but I think we want just one random, more structured way, right more structured way and more official so that we can for each of this decision, we can basically document that rather than some ad hoc or offline discussion, which is sometimes quite hard to check. This is a we make videos of this forum to list out all the changes or the design review that we have made right so that that is more structured way to to manage it. Yeah.

Okay, okay.

Yeah. So so you're I think this the team VLANs is representing architecture. So we put VLANs your name here as well. So from our site, we expect the chromosomes to be on a call. Is there anything else missing our VLANs Palumbi project manager? Project Support means out Okay, so we lost your name as well. Okay. Any question for us? No, no entrepreneur. Any things you want to add? Praveen.

Okay, let's

just also highlight to Chennai is the permanent delegate for chairing this meeting. So Chennai would be considered the chair of the meeting, I will just join in on an optional basis. When when time permits that to educate. I've got a permanent delegation.

Okay, so I think today sorry today, we will send out the agenda. But I dropped an email yesterday but in the future, we will put it in more structured way for the agenda. So I think the we have one open topic that I have not I don't think we have close it, which is VTS.

AX Can you send me

Okay, yeah, so I think we just want to close off the DTS tokens solution. So, the topic how we, I think the how we block and unblock tokens we have discussed but every move off tokens I still have that close right. So just want to close this topic and also the topic being raised is what the batch file management. I think there are some a couple of incidents on that happened on our site that we also want to really look at the batch file management approach and see how we can avoid such problems. On top of that, we also want to start to pick up the some of the topics that are open. Right. So let me go through the topics I don't I'm not sure whether we we have any thing ready for the discussion. First topic is, I think when we started the project right, so in terms of how we authenticate the how they run API being authenticated, at a point I want to send that basic office use, right. So I think we'll do correct some of the security posture our bang actually don't allow the basic off. Right. So we will want to explore whether there's an insecure, more secure way to protect the API on both sides. Basically, to make use of all four mtrs self basic of Yeah. So that's Topic number ONE. Topic number two, I think this has been outstanding for a long time. Because of the go live, and we delay this and slows urgency per se, is to how to reestablish a connectivity to your own physical data center for the DR site. So right now we are making use of VPN, right to visit our data center. So I think now is to talk about how we can relook at the design to move it to direct connect right so we can make use of the private link rather than the VPN approach. That is for the to have a separation of the endpoint for the authorization and a few transactions, right so that we don't have to be hogging the single endpoints. So I think there's also some comment as one of the top leads of the issue of urinary is the stability of the nonprofit environment. So actually, it is causing a lot of inefficiency in terms of testing and for the project rollout. So these are the four main topics.

So I think to start with maybe let's talk about the first topic, I think this should be quite easy because I think that design is already ready. We just have to go through the design and then close it off. Right. So yeah, so I think maybe I know you take over the screen and walk us through the design on the first step. You have any diagrams or design material to show?

Sorry, anything to answer, Hassan and Prophet

No, I did. Let's just focus on today. Let's just focus in on token management, if possible, but I think I think it needs to be it doesn't necessarily need to be like we close one topic at a time, right? We can just say open management. And if the if the action item that we need to take is to say, finalize the full lifecycle of token management, create, update. Be activate, delete. lifecycle events to throw it come to this forum on the next one, that's fine. Let's just the target would be to just keep these high priority topics more so that so that we don't lose them. So if you don't have anything for a particular topic today, that's fine. Let's just call it out and say we don't have any updates

for this court to convert to we have circled one diagram last time, okay. I'll show you Okay, whether that is sufficient or you want to

display just confirm if it has been seeing on display dot pdf.

Are you able to see my screen

yep yeah

okay

actually Dizzy this is the flow girl. We have all this tokenization is happening. Okay. How the what are the changes we have done for this change, which is I think, plan for next week, I guess. Last, are you sharing your screen?

I'm seeing the screen. I can see the screen we can see the screen. Yes. I think we lost the previous call. I was there. So I think from one to six. We are quite clear what is done. Maybe from seven onwards. That's where we stop. Yeah.

Yeah. Okay. So, right now right. We are just giving this respond, respond to Phoenix, okay. And we are moving this particular step particular state status and that particular card right. We are moving to a one of my one of my file okay to send this token to now token to visa or visa and we are updating that particular token and we're sending this one one by one token to

visa. Okay, suppose

much. Suppose I'm taking example of Chinese merchandise card right? Suppose Chennai has one card in his card. Right? So to reply to that particular request, right, we are just doing this one card at our RN, okay, downtown card base and we are just sending sending requests sending reply to you. And on backend right. We are moving that particular particular request. Request right to five to file that now can now for 10 minutes god okay send all the token token to visa okay and that this is this we are doing the backend okay. And one by one we are sending the sending all the token to token to visa Okay. In case okay if there is there is any timeout for that particular token right. It will go on it will go in the standing standing in the standing file okay and it will it will remain or the Okay. Once the network connection between visa in my mind is up. Okay. The time I'm sending log on. Once I'm getting a lot one response and then fitting the second next request and I'm sending a request to visa. This is how much torrent for for works.

Okay, so you're saying this is already done my so we're going to roll out

yeah, this is a clip. Actually this is a tested the testing result we have shared with the bank. Okay, and I think this is shared next week. Ma'am. Can you also have the exact date if we are planning

declines So as per my discussions with Karthik a still approvals are pending from bank and and also your internal approvals are pending, but then as we have discussed it is scheduled for Monday night that is 27 March. Okay. Oh, I did that was a close at both ends.

Okay, one one question. Can you move up a little bit? Yeah, sure. Yeah. So for step one to start right. So you will look to each of the cards and fire code will be start to block it one by one, right. So stone forward model. Let's say do you do have any number? How long for one cycle to complete? Let's say for each card, how long it takes to complete

feed depends. Generic ma okay. Okay no problem. How will you feel if you have no three or four tokens from from Viet from visa right. We are sending 1302 message and we are getting 3312 message from visa right it is it is happening happening in milliseconds. I

click OK. Okay.

So normally right in Arduino, right? Tell you 10 card, right? It should happen in seconds. Okay, okay, two or three seconds. Okay. So this is this is idle.

So but let's say this guy has a lot of cancer would take definitely more than take example

of Hassan 7675 Seven token let's say so. So it so it will take four, four or 5855 seconds.

Okay. Okay. All right. So, my question is this right. So, this four or five second while you looping through this and trying to apply each of this digital token right. So and during this interval, the user come back and unable unlock the cap. Right so now you have half of the digital data we call that depending

lock condition and then before you complete

the rest of the user come to unlock it never gonna happen.

Yeah, see, too easy to go and it will sit in queue Okay. Suppose you are how you are in a process and you will complete half of a request, right? Suppose now Hassan has 78 to convert and suppose we have sent 3434 35 tokens to visa and in between that Hassan has come and he has changed his state status again right. So it will go into it will sit in queue because your first request is not completed. So it complete first request and then it will go for a second second request.

Okay, so you will need to complete the cycle to lock it and then go to the callback to the next queue. To unlock it.

It will go into check whether this particular car right whether there is there is any pending pending request in a queue. So if if there is any pending request in our queue right, it will need to sit in queue until unless your first request is complete. Once your first because it's complete then it will go for a second request.

Okay, got it. So I think Can I request you right? To this additional exceptions in our real put a small time, like when like this, to indicate that there's a let's say the meat of the processing right? The user changes things, then that check that you describe, just have to indicate that Yeah.

Okay, so you want the diagram

or diagram or somewhere you can indicate here, okay, okay. Okay. I tend to prefer one

quick one. Better features, maintain a state on the other side to say if if you have ongoing status change happening with Visa. You're not allowed to do any more status changes. Then cueing these 100 times because I don't know what will happen is if somebody is playing with the UI, lock, unlock lock unlock pages. I mean, isn't it better to have a state Okay, internal state in you're gonna do that.

Let me ask a question. So have you lost at number 10? Right this is per depend or is is the one call for all the status change number 10. Three, one by one one by one. One by one. Yeah. So that means probably if we do that, that means we can do a counter to reconcile how many has been on

I'm feeling I'm saying, Okay, so before this, right, I'm saying go back all the way to the top. Right. So I'm saying after three, four, right liquid validation card status. Update, post successful validation all of the disk access. From this point, until the rain API server, complete the full process with Visa on the token status sync the card should not be able to go through another status change.

Yeah, so in order to find out that and number 10. We have to track the user have how many Deepan? Right. So

I'm saying don't use the call back to count it. user error code is the status quo. So if the UI said something you just said sorry. Existing the previous card request, it's still in progress.

Okay, so that means that's part number eight being process. Number one, come in again, right, you don't get that number three, you should respond with a record instead of changing the cup.

Because to be honest, there's nothing happening, even if you accept one there's actually no blocking happening. Just one telling the user it's accepted.

See, actually no, actually, no we need to allow users to do or not do a status change we should not know hold. Hold a customer to do the status change okay. Because there is a possibility right see, it will happen practically suppose he wants to hotlist car because of some XYZ reason right? If you are holding right, your status is a status that will in my database, that particular fraction of second second time right data data was so the possibility right. So it is better that no, you should not you should not allow and you should at least you to roll to cause her to change her mind. She took her shirt as I'm doing separate separately that is okay, but at least I am. I am declaring the transition straightaway okay, because we're car status is not listed right. So so I can declare that mine only only to see I'm sending sending data separately to visa right but on the basis of card right I'm straightaway declaring the promise and this is this I can take a decision right right away, right. So I cannot wait

so basically your main into separate statuses and I correct to say that use male character, okay. So character level and the level Correct? Yeah. So you're saying the card level, let them flip anytime, but at a card token level, you will queue it. Yes, you will. I will handle that.

I think that's better because if you screw up the one of the tokens status, right, you also need that particular wallet can use rather than we hold back the card status change. Right you unlock a lock unlock maybe for some urgent reason.

Exactly, exactly. Correct.

Okay, I think maybe we just have to document that exceptions in order because we might be forgot about this. This way. How is this being handled right? In the future? So just put a note to indicate how free exception how we handle that Yeah.

I will. I will use the given writer. Okay. Maybe I will give I will add one writer but I'll send two.

Okay. Okay. Fine. Okay, right Praveen Vikram.

Okay. So, but tonight, we only want to close the status change or do we want to consider lifecycle management for this topic. I mean, if you want to close just a status change, I'm fine with it. But I think one of the pieces that I thought would be good is to talk about the entire lifecycle management of the heart tokens to create status changes. And deletions, which we haven't really touched upon.

I think for that one, it's better for me to talk to her son whether we want to do that. God's the test actually, there's no bank do the token lifecycle. Even besides this, I quoted why is that as the only the vault can use? There's something not as not so simple to check the total lifecycle on our site. And what is the purpose what is objective at the end of the day when we want to show do that is only show the user whether that volume is active or not? There is no other value of doing that.

But where is the who, who is doing the I'm not saying talk. I'm not talking about showing something to the user. I'm just trying to understand the end to end card token lifecycle

is on your intranet.

Okay, and then what happens to expire deleted your views

during the season. This is triggered to muscles right when I was supposed car is caught is expired, right? So Visa has no reason code right? Like 70037014 Hartleys 3703 For resume, like resume one. So whenever I'm doing doing any action right, on card right suppose a card is replaced, right? So we need to send 372 When cards expire, right and to send, send expiry to is that time I'm saying to seven, seven to zero, right? So this message isn't good, right? I'm sending in this message. So whenever whenever card expires, so we need to I need to send this message to visa so that visa and visa and they are changing the exponent of card

right now, and then whatever they do send on Arrow number eight per card token comes back to us in arrow number 10.

Kind of got a good yield or whatever I'm sending to I am going to go to send one message to use your CVs.

So which, so which endpoint is this number 10. Which endpoint is it hitting on our end? Or you will

check the import? Okay, I think we have received I think this is different endpoint I guess.

Different different, different

is different. We have a dedicated endpoint for the VTS. Psycho. Yeah, it's not part of the urine. transactional

work competition. We're using several different endpoint and token we're using a different point.

So we have a dedicated point for the BTS. The reason why we capture this is only for the is it's important for the registration because we send it to our cut fraud. Other than that the lifecycle actually, there's no requirement to maintain the lifecycle on our on our site, and it's very complex to do the reconciliation. Right.

So then we currently receive them and

then we receive them we update, but then after the just just the registration is correct. The lifecycle actually is already out of saying your body's disabled delete,

to recall them and check them maybe Can I ask you to take this, but draw, draw the left hand of Arrow number 10, just so that we've completed the picture, and just say, on the trust side once we get number 10 or 10? A, this is what we do. Oh, that the picture is more complete.

We have the sequence diagram already. Yeah. Okay. Cool.

Thanks. So that both one both teams are aware of what we're doing with it, too. It's a more complete way to display the solution.

We have the sequence diagram, will it be Let me check. Yeah.

And one last question. Is there a possibility and then we can maybe do something for us to take internally. Have we thought about segregating these kinds of updates that are coming back to us from the old traffic like being able to navigate that traffic away from the ports that are taking the old endpoint hit

something I don't think currently sadly, probably.

So So can you repeat the question?

So any of these administrative kinda callbacks that we get from

ETS bureau?

Not necessary, not necessarily only for this but I think what I'm trying to get is, How do we separate out the network? Professional Network, the third level separation to get the callbacks to be on a different priority queue. Rather than getting through the same pipe as the old transactions. So that way, all of this just gets listened passed on, but it doesn't affect the same pot that can

vote. Okay. I think that's good point, because now it's the same pot. That processes but different end points.

Yeah, okay. Maybe it's an internal action item for us to take care

of probably now you're seeing a difference, or is it a basically a delete?

I think I think let's just internally discuss what would be the best way whether whether it is whether to use the same port, listen to everything, but only pack these in a queue and let the downstream process them slowly. Or do we want to go one step further and start building a pattern for Euro net to send us advices or callbacks on a completely separated path? So that way, we know for a fact even if there's a major let's say let's let's say let's say like there was a magic up on the on the Euronet side, right? Let's say somebody just started playing with the car lock unlock 200 times, and they did it together with 20 other friends. When those requests start flooding us back, we know for a fact that will not affect the same ports that look at both transaction

and then we can take off like the second option, actually very easy to do. Yeah.

Okay, okay. Let's

keep let's keep that on the internal side of the design. Yeah. I mean, at least as a consideration, we'll come back and then confirm to this forum as well. What we designed internally because I think it's important for the unit team also understand how we deal with it.

Canada if you're designing that, right, whatever you're sending to visa right, it's one by one message right one message has to complete then I will send a second message even though you are 60 but 70 by to convert so I will say one by one, maximum maximum to contract, a one can one can generate for one car is 99. So he can't do so. So if you're taking decision, just take the decision accordingly.

Yeah. And so instead of one, one token at a time to visa per customer or

customer. One, one, recent one request to visa if we complete we send second visa we expect the message to come.

We'll ask can I just ask a slightly different question What if one of our back office processes make up all of a sudden decide to undercut fraudulant decide to go ahead and block all do on it.

You're rocking this card and my following current mind right? I need to just send messages to visa so that I can say but you are blocking your heart and mind that you can do it instantly.

Yeah, I understand. So let's say 200 into imagine all of them use their 99 tokens to undertake consists with keeping the calculations insane. So that's 20,000 request. Are you saying you're only processing one transaction at a time for that? 20,000 are you parallely sending them to visa it's

a it will go parallel to visa but room for 111 card it is a one to one request to the consulate.

So you look through the cards token by card ID.

Okay,

I think anything else for this token topic, maybe we lost just have to update that. I can attach an we can close this topic. If nothing else.

Anybody's tracking deleted or expired. Like what? Any any documentation around how what do we do with those tokens?

We capture that status and update on our site? But then the thing is, if some time this request is better, it's really a great consult. We never do the reconciliation. Yeah.

I mean, for example, can we delete a token? For example,

you can because the customer can delete or remove the token from the wallet. Right? So if you run that we send that request to us to update our site so we capture that status. Right now. Just the only thing that we never reconciled

and they forever labor in Euronet like they never get removed from the European system.

I'm not sure Yeah.

Your newspaper status. We are not deleting that record from my TV. The status will remain. No, we're only changing the status. We're not removed that deleted the data.

But as a status list, it will ask that you maintain for your tokens.

It's active along the way, but for free for finish right there. We have some other tokens. These are standard tokens. This is what PISA is, I think one can do but finish right? We help we help keep some different different response code.

Okay, hold on.

Can I also just just a new question what is what is warm stands for is that for like keeping it block? Every block

will tell you okay? This is this is we have descriptors okay, if you're able to see my screen right

now see, okay. This is permanent block, right. This is this status in Phoenix has meant that your index permanent block, right. This this temporary block upon block

nobodies are they but these we maintain at a card level? I'm asking for the tokens because we don't maintain any status as for tokens in inside

token token only now we are sending active Wileman block that's it. No other. This card is for token.

So whenever you get a request for the cards to change, do you go through the full token list or do you only go through active and warm token list? Only active so basically the activated tokens just stay in your system. But they never get hold up. Yes.

Okay

any other questions for this? Otherwise we move to next I

think I think before we move, let's just agree on the action items we took for this topic. So I think you're gonna update the high level solution designed to document what happens for the API call that comes to do the status change while existing token status changes ongoing. Alright, use that I will, then I will have to do an internal check. Now I think we have two action items, which is to update the trust side of what happens when that 10 equal 10 Call Number 10 call comes in. What do we do in that API endpoint? And also, internally for us to discuss whether we want to deal with a separate network path for these callbacks or not? Okay to demise the to minimize the effect on both transactions. Okay. Do we have time for another topic?

I think there are many topics I'm not sure whether Euronet team ready for discussion. If not, then I think at least we prioritize which topic do we want to take on next right? So one and two has been there. For a long time. And now even we gotten disability from the VA j. So this point, I think is what related to what Praveen mentioned, right to split the authorization endpoint. I think four is a constant ongoing pain point. The batch file management I think is raised by Karthik is not clear.

I think to guess I think I think his point was sorry. I think maybe this for Rick and Allah me to confirm we've had from what I heard last time. We've had a series of incidents over the last couple of months where we got the wrong batch file coming across the Trust Bank. Now happy to be corrected if I have got the wrong version. However, the purpose of the reason why this topic was raised for this forum was for us to discuss the full lifecycle of your clearing batch file, for example, how do you get what you get? How do you generate the file? What validation points do you internally to ensure that that is the correct file for that correct date? And how do you send it across to us? What control checks that we could implement upfront before we process the file to understand whether it is the correct file? Who's tracking the frequency who's tracking availability of those endpoints, etc. So are there any documentation Vilas on your end that shows the clearing file batch processing on your end? Clearing fathers the right word but I'm using I

think we have given one document for clearing file okay. And knowing that the thing to file how file it is already mentioned in the document,

we have log back. So if you want I'll refer to it after this call because that was prepared by our operations team. And we submitted that Yeah.

Okay. So the reason that and we will revalidate the design, but I think this topic will remain open until we get a bit more clarity, I would say on both sides. So basically Parliament villas, if you can just please send us all the batch files that you guys are currently processing and sending for us and any architectural details at all. What is in those files? How does the file works? How what is the control file looks like? What are the control points that you enable on your end to validate that your file is correct? What are the frequencies who's monitoring the frequency that it is actually happening or not happening? And and then, once we have that information, we will check internally to double check. What are the control that we could take ourselves to validate whether a given file is the correct file before we start processing because I believe you've had a certain amount of production issues trying to process the file that you send to us that apparently had the wrong place transactions. So we've gone from taking the file processing it instead of validating things about is destroyed file to begin with.

So yeah, the agenda and pretty normal just requested so we have we have submitted a document, but just to have a double check before resubmitting it. On this on this topic. Can you just jot down agenda if you can, the expectations in the document then we will reach and add something if it's missing. So then we don't have iterations of the document.

Okay, yeah, I mean, again, right happy to happy to reply again. So basically, we are looking at what are all your batch files? How are those processes in your end? What are the frequencies for those batch files? What are the control files for those batch files? Who's monitoring the frequency? And what automated quality gates you maintain on your end to make sure that the files that you generate for the day is the correct file. Once we get that information, we will check internally what controls we could put in place to make sure that we don't process the wrong platform, which is what has have been for the last couple of production issues we've had around this topic. Is that care

revenue anything to add on to that right? So one issue that we noticed was like we had some special characters in the transaction record. Maybe we can list out the agreement to say like what special characters are supported in the file. I think that also helps us to identify if there is any issue with us.

I think that's let's get to Vikram. I think maybe like again, right? You don't It is one of the earliest systems that we integrated so I'm pretty sure we didn't do a lot of documentation around it. For the for all these batch files. Let's just start documenting what is the structure what is the data format expected? For each one of those fields? Etc. Because I don't think we've done that piece of work back then. We just went ahead did it. Okay, that's that's what was needed at the time. So let's use this opportunity to start documenting the full that's why I said not just don't look at one file. Let's use this opportunity to look at all the batch files that are coming in. It's more human to frequencies. This document when are we expecting it when are we expect processor all of that so we can use this information and feed it to our batch file list as well.

So I think internally one thing that we might need to consider is like if there is any failure is another request. So we don't stop that batch. instead. We continue the crossing I think currently the designers if there is an issue with the last record, we just failed and that's promising.

So what we'll do is I'll just what I'll do is I'll just add an additional in additional point of the discussion, so that maybe next time when we are here, with more information, we can break it down to more cleaner action items, and then put them into your backlog.

Edge to edge. Really talking about the batch file right off my apologies. I just ended up with a Colin joint over

here. Yeah, you know, we know just talking to you on a team about So we've asked them to share us few information. So one, the full list of pitfalls that we are getting from Euronet file formats the control file format, the frequencies, the internal, any internal documentation that they have around the lifecycle of that batch file. And what what quality case they implement on there and for each one of those batch files, once we get that to do internal analysis and come back to this forum to discuss what would be potential extents?

Yes, I think well, let me just share the batch file for batch file we had an entire document the I will see the standard document with document all the requirements that we had given. It might not have the technical details, but share that as a full document after this one. But I think here the main thing is big. And probably we have to look at what they could have just mentioned. That was Record filter data that will determine and at the human level some kind of an ID because you don't know the biggest fear I have is when a batch file is we don't duplicate process to batch file because that means $150,000 might be duplicate posted which has happened twice. And we had to spend probably two nights just to ensure that that isn't nearly 50,000 Now we want 250,000 transactions over there. So I think for that the team was it again, the architecture team question over the lesson we should work if he has some unique too on the same level identifier that we can put in a idempotency at that level. So again, these are the discussions so I just wanted to share that is what I had discussed with me earlier on and

I will I will put a topic here but I think these are more internal. But let's let's again, right let's look at the files first. And then we'll decide what are the next action items that will fall out from that?

Because the reason I'm saying that that while they should it has to come in that batch file from your audit then only will be able to recognize that over there which is not available at the moment.

Great Again, rather than just going into one. Let's just first close the full view. full batch file list, File Format Control File Format frequencies, overall lifecycle of that batch file management, any documentation from you donate about it. What are the quality control gets implemented within you met and who's monitoring the frequencies? Let's get that first and then we'll break down and agree on action items going from the top Yeah.

Okay, so I would take that batch file management and the analysis would be the highest priority and other than that, we have these four topics being listed right, I think, I'm not sure. Philanthropy for me TV prepare anything for this. Anything for the discussion for this, okay, I think let's maybe let's prioritize which one to top next. For our next session. I will say the authorization that API authorization is one of the items that we want to look at. Yeah, one to one I would like to understand from you right, valence. So when we started, the only moto support is basic off. Now. Is there anything that that the rent API has been proved that since support, often MTLS or MTLS

check now we are supporting this or not? Okay. But I'll check in and come back to you on this. Okay. We can implementation but we are we are supporting but let me check. I'll come back. Okay.

Okay. So maybe if possible, you will come back that and if there's anything that you think can be shared earlier before our next session, you probably can send us first and we also get ready for the discussion on this topic.

Okay, okay.

I don't think this this will be a complex topic. And if you are supporting then I think we just have to plan on how we switch to one of this model. Correct? Correct. So probably not assuming this topic you want to prioritize separation of endpoint for orphan few transactions,

I think. I think what we'll do is we'll make it for the next call. Yeah, so let's just try to close the I think hopefully by next one, we can close the full visa token. Removal topic. We will be still keeping the batch file management process open. And let's close the security concerns as an expert in reaching out to the API authentication. Once that is done, we will talk about the port versus failed card transactions. Okay. So sorry, just for the guys on the call from Euronet team. The ask here is to separate out the valid and valid votes 10 points from failed car transaction callbacks. The simplest reason being if there's a if there's a pain range attack on our bean range, we don't want our internals stems to get choked on the wrong fail car transaction process. isn't clear to ask. You can clear

this order right in order right now for this is for termination automate. I'm sorry. I'm sending you one one important, right? And whatever permissions we're declaring my right right for that, well, I'm sending sending you a one RS message. It was message to the finish this correct, right

yeah, to the last day requested that the advice message can be sent to a different endpoint that is a request.

Different input, right. So whatever, whatever I was gonna say right now I'm sending whatever I'm declaring. We can only send two different input right.

Okay. That that require that the request for public Yeah,

okay, that can be reasonable.

Okay, maybe if it is if it is a simpler one, then maybe we'll push it up on the priority list simply because this will help us to stand up properly and against being injured. Because otherwise we will we will crash internally. The first time we go through been rich. And sorry, the fourth one, which is stability of nonprofit environments. We couldn't before the next meeting, do you think we Clint Watson, do you think we would be able to get a few concrete examples?

I think I've made a lot. Yeah.

Yeah. Yeah. So probably I think for this we are we were fixing some of the issues with the nonprofit enrollment but looks like now it's pretty stable. But yeah, we will try to get the failures, what we encountered over the last week, and probably we can show it but I think it's pretty much stable compared to what it was.

So what we'll do is we'll just keep it on a low priority for now. We will only pick it up once if everything else is closed. Yeah.

I think Praveen for the last one I would say that led to the commander of monitor that if we still face then we keep it on the agent over it. But if you don't see failure, then we can we can give you the confirmation before the next meeting. You can just remove it. Okay. What is the first one which is the visa token removal flows? Is that something which is closer to what is pending or that

there were few action items I think I think we agreed to document a bit on what happens on our site when we receive it. And to document what happens when a parallel status change call happens during a token process. I don't think we managed to get to the retry mechanism related conversations right? Like what happens if we are unavailable

that this conversion rate is it is on male with Hassan video is not documented anywhere. So you want especially talking about like just like the flow.

Update the architecture diagram itself. Yeah.

Okay, okay. Yes, I think so. We're not I would just say to that over there, because Praveen, we've concluded the testing and just to let you know, we're coming live with it in production. Monday, or sorry, Tuesday morning over there, too. If you can, let me know know, because the testing or everything is approved. So I just wanted to ensure what the bill has confirmed over email two weekends ago. You were copied in that one as well. Let's document that. If that meets your requirements. Let me know if it doesn't meet. Then let's just get on a quick call and get those things documented. So that you will

actually speaking of which I think it's good to get things out of emails and put them into architecture diagrams, will ask can you update this document to call out for every API that you are making towards us? Can you document on a table at the bottom module retry mechanism is okay so let's say for the older web hooks that we have given you so for example number 10. In this case, is the only web hook you're using right now, what is your retry mechanism with the back? So if we are unavailable or if we keep giving you an error, what would you do? Like I think we need to start documenting error handling process.

This is this we had no discussion of the person and reading this document it maybe we will share the document with you.

Yeah, I think what what?

No, I'm just trying to say when we make high level architecture diagrams for us, our references here on wherever we are using web books, and China, maybe we should do the same on our end as well, right? Like when we are calling the API's directly, we should document and say what is our retry mechanism because our retry mechanism might be just try three times if it fails drop. Like for the status change API, maybe that's what we're doing right? Maybe we only sending tried three times. If it fails, we don't try anymore. Likewise, I think we should document from their perspective. Whenever there is what is the retry mechanism like when you call us will ask what are you going to do? Are you going to do exponential back off three retries? Are you going to do sub second three retries. And if all retries fail, what do you do? I think we need to just put them in the architecture documentation because these things get lost in emails with us.

Okay

because they give it that establishes forum over there is documented and they say this from an audit perspective is the right way to do it over the emails. We'll get things out. I will miss the email. Maybe we just have to go with I think this is the first time around but going forward. This is the forum that we have all the things documentation over there. I think that establishing it now. We just this one time do

you have one final form

I don't think we should go through the rest of the topics for today's and I think given us the first one let's just keep it light.

So the not to start next topic next week but I think we also need to get our stuff ready for the discussion of moving the from VPN the direct connect right so how should we plan this? I'm not sure whether we are ready to have anything to discuss for our next session. But somehow we still have to plan for this.

Can I just quickly verify something for our last year? What did we do? Did we have this or did we not have this far last year VPN? Okay, so how often do you roughly remember when we did the last year was it? August?

July, July to learn

Okay, so given this a PC five we need to redo our TR before July. Exactly. So if we if we need to change something on the connectivity, then let's just discuss it sooner. Because I mean, if you're gonna change the path, but the next year, then we might as well progress is over some of the other stuff.

But why? I mean, I would just switch to revenue I would recommend that and the reason being is that last year when we did the Dr. Praveen it was a very quick 20 minutes to year over there. But now given that we are a bank with quite a sizable number of customers. I would want to run a deal for at least a couple of days and all the processes are working over there before we move back. Again, the connectivity will be because it is the deer was beta 1000 customer didn't really bite. Now it matters a lot.

I think now given this already mastered July I'm not sure whether there's enough time for us to complete the design and to the switch. Right before we do the Dr. Then after we do a search I think we still need a period of time to do the testing right. So probably we can start to talk about the design. But to change the change I think probably is better to do it after the because at least we know BPN is working but how good is PayPal to the scale,

but

Okay, again, I think maybe we will have to reverse the conversation. If husband wants to keep the DRL live for more than a day. I'm comfortable doing it over VPN.

And then the question is basically Praveen is that and last time we did the Dr. It was barely like 1000 calls a day. Now we don't know what 150,000 foundation so is VPN stable. Enough for Harbin 50,000 pa they hit the auto which almost 130,000 come only in eight to 10 hours. When people support there are no laughs If this is something we are on, they come back and as a team again, this is the taking 30 over that discuss that he even did the we will keep it very limited at night for 2030 minutes from a response. Perspective. Are we okay with that or that or the other one is that if this design takes longer, do we want to take a call that we push out the dry couple of months we want to do it the right way. So again, I'm just taking the opportunity here internally. So a grid

Okay, let's think about it there because now it's already April. So we have about three months to design and switch.

Yeah, I mean, no other person right. I think it's a little late to plan but I agree with China. I mean, I think we don't plan over the years fine enough to which then leads to these kinds of situations where we won't do something before next day. And then we're now stuck because we only have two months to go before that. happen. I think that decision on how long do we want to run out the for BC file systems that are hosted by third party? I think we need to make that decision together with Raj and Johnson wants to agree, but they what they want to do for the time period. Then we will come back to this decision to ask are we comfortable doing this Oh VPN. I mean, for example, when we did it, we don't even have VPN monitoring, right? We just enable the VPN. Exactly. Keep it on. So if you're gonna keep it for like 24 hours or 48 hours, it's going to be a very tricky one. So let's, let's have that chat with Jensen and Roger first the other risk owners for the DIA. And once they agree what is the time period they want to keep a b c five d I'll go and then we will come back to this.

Okay. I think maybe we lost I Can I request. Okay, let's put the timeline aside. The thing for this to work right the majority of the efforts on your site right so because now we cannot direct connect us we cannot do private link to your site in Mumbai. You need to have a hop in the Singapore site and do a direct connect from the physical data center to the Singapore AWS I think maybe we can start the design and you come with some proposal. Then we see what are the options possible options Yeah.

Okay. I will discuss with my team on a duty

to involve network team so we are putting this topic again in the agenda for the next meeting. I will also get my network solution. Person and team.

Okay. Yeah, so I think this one I will put more specifically to for the design proposed design design review first. We don't talk about the setup. So everyone is a little bit okay. I think, Bobby, that's all for now. Is there any other topics? Hassan and Praveen you want to bring up?

Nothing, just one point. is fun. I think we'll just change the add the documentation that we've requested for in the lock unlock and the token flow design over the site across to Premiere Pro. We'll have a look at that one. Let's just close this off this piece of employee for Monday because I just want to close this off before we go with the deployment.

Yeah, so the points are noted on the update sorry, Chennai while we were having the chat, I also update the page. So the action item is to update the high level solution design page to meet the parallel status quo. What happened to that? And then also to add the retry logic to the architecture documentation. All right, cool. Thanks, guys. Good to go.'''


s = summarize_article(txt)
print(s)
