import json, re
cats={}
cats['Attitude']='''I know my worth, so I never beg for attention.
Silence becomes powerful when there is nothing worth explaining.
I walk my own path, even when the crowd chooses another road.
Dignity will always matter more to me than temporary approval.
I do not chase people; I protect my purpose.
Peace is too valuable to trade for unnecessary drama.
I respect everyone, but trust is earned slowly.
I am not competing with anyone; I am building my own lane.
The moment respect disappears, so does my presence.
I would rather lose people than lose myself.
My confidence was built from battles nobody saw.
Not every opinion deserves a reaction from me.
I stopped proving myself when I realized my actions were enough.
Being misunderstood is easier than pretending to be someone else.
I keep my circle small because peace needs space.
My boundaries are not attitude; they are self-respect.
I do not need a crowd to feel secure in who I am.
Some exits are necessary when staying costs your peace.
I can be kind without being easy to take for granted.
My standards grew higher when my self-respect grew stronger.
I do not return to places that taught me how to leave.
My calmness is not weakness; it is self-control.
I have nothing to prove to people committed to doubting me.
I choose authenticity even when it makes me stand alone.
If the energy feels wrong, I do not force the connection.
I do not hold grudges; I simply remember lessons.
The strongest response is often a life lived well.
I am selective with my energy because I know its value.
My absence is not punishment; sometimes it is protection.
I stopped explaining my heart to people who only wanted a reason to judge it.
I do not need permission to become a better version of myself.
Respect is mutual, and I never ask for what I am unwilling to give.
I leave quietly when the situation no longer deserves my effort.
I am comfortable being the person who chooses peace first.
My self-respect does not depend on who stays.
I do not follow trends when I can follow my principles.
I can forgive someone without giving them the same access again.
My life is too short for conversations that go nowhere.
I do not confuse attention with genuine respect.
I would rather be alone than accepted for a version that is not me.
My standards are not high; they are simply honest.
I learned to say no without writing an apology afterward.
I do not need to win every argument; I need to protect my peace.
People can misunderstand my distance, but they cannot control it.
I became quieter when I learned that not every battle deserves me.
I am not cold; I just stopped giving warmth where it was wasted.
My character matters more to me than my reputation.
I do not chase validation from people who cannot value themselves.
The less I force, the more naturally the right things remain.
I choose progress over proving a point.
My standards became boundaries after enough lessons.
I know when to speak, and I know when silence says enough.
I do not fear starting over when staying means losing myself.
I am proud of the person I became without an audience.
My energy belongs to growth, not gossip.
I do not need revenge when distance already says everything.
The right people never require me to beg for basic respect.
I can stand alone without feeling incomplete.
My confidence does not need to be loud.
I stopped taking everything personally when I learned people reveal themselves.
I do not compete for places where I should be valued naturally.
My peace is my favorite kind of success.
I would rather have a clear conscience than a perfect image.
I do not owe everyone access to my life.
I protect my name by protecting my choices.
Some people only miss you when they lose access to you.
I do not become smaller to make insecure people comfortable.
My patience has limits, and my boundaries have reasons.
I choose distance over disrespect every time.
I do not need to announce my growth; people will notice the difference.
My strongest flex is being at peace with myself.
I can walk away without turning the exit into a scene.
I stopped chasing explanations from people who gave me confusion.
I do not let temporary people create permanent doubts.
My life gets better when I stop entertaining what drains me.
I respect my past without letting it control my present.
I am not difficult; I simply know what I will no longer accept.
My silence is sometimes the clearest answer I can give.
I do not need to be liked to remain true to myself.
The older I get, the more I value peace over popularity.
I learned that self-respect sometimes looks like leaving.
I am not afraid of losing a connection that costs my identity.
My priorities changed when I understood how valuable time is.
I do not chase what requires me to abandon myself.
My confidence grew every time I kept a promise to myself.
I choose people who bring clarity, not confusion.
I do not argue with chaos; I remove myself from it.
My standards protect the life I am trying to build.
I can be soft-hearted and still have strong boundaries.
I do not need to respond to every rumor about me.
My peace does not require everyone to understand me.
I am done negotiating with disrespect.
The best version of me does not need everyone's approval.
I leave room for people who know how to value it.
I am not chasing attention when I already have direction.
My attitude is simply the confidence of knowing who I am.
I do not regret outgrowing what once felt familiar.
I choose self-respect, even when it makes the road quieter.
I am enough without having to convince anyone.'''.splitlines()

cats['Love']='''Loving you feels like finding home in a person.
Your smile can turn an ordinary day into a memory.
My heart feels safest when I am close to you.
I would choose you in every version of this life.
You are the reason some days feel worth remembering.
With you, even silence feels warm.
I never knew peace could look so much like a person.
Your presence makes the little moments feel important.
I want a lifetime filled with ordinary days beside you.
You make my heart slow down in the best way.
I love the way you make me feel understood.
Somewhere between friendship and forever, I found you.
You are my favorite thought at the end of the day.
I would rather share a simple life with you than a perfect one without you.
Your happiness has a special place in my heart.
I still smile when your name appears on my screen.
You make love feel gentle instead of complicated.
My favorite memories somehow keep finding you in them.
I want to grow old and still look at you like the beginning.
You are the person I want beside me when life gets messy.
I never get tired of choosing you.
Your voice has a way of making difficult days softer.
I love the little things about you that nobody else notices.
You make ordinary conversations feel unforgettable.
My heart knows your name better than any song.
If home had a heartbeat, I think it would sound like yours.
I want to collect moments with you, not things.
You are my favorite part of an otherwise ordinary day.
I love you in the quiet moments just as much as the exciting ones.
You make my world feel less heavy.
I want to be the person you feel safe telling everything to.
Your hand in mine is still one of my favorite feelings.
I did not plan to love you; my heart simply recognized you.
You make forever sound less frightening.
I love how easily you can make me smile.
You are the kind of person I want in every chapter.
My heart feels lighter whenever you are near.
I would choose your company over a thousand distractions.
You are not perfect, and that is part of what makes you precious to me.
I love the person I become when I am around you.
Your kindness is one of the reasons my heart stayed.
I want to know every version of you life creates.
You are the calm my heart never knew it needed.
Every little moment with you feels worth keeping.
I want to make memories that age beautifully with us.
Your laugh is one of my favorite sounds in the world.
I love that I can be completely myself around you.
You make even boring days feel like something special.
I would still choose you on the difficult days.
Your love feels like a quiet light in a noisy world.
I want to be there for the days you feel unstoppable and the days you do not.
You are the person I want to tell my smallest stories to.
I never want to take your presence for granted.
Your eyes still make my heart forget what it was saying.
I love how safe honesty feels between us.
You make me believe that good love can be peaceful.
I would rather build slowly with you than rush into something temporary.
You are one of the best things my life did not plan for.
My favorite future is the one where you are still beside me.
I love the way you remember little details about me.
You make distance feel temporary when the heart is certain.
I want to celebrate your wins as if they were my own.
Your presence is a gift I notice even on normal days.
I want to be your comfort after a long day.
You are the person my heart searches for in a crowded room.
I love how your existence makes my world softer.
If I could keep one feeling forever, it would be this feeling of us.
You make me want to believe in lasting things.
I want more sunsets, late-night talks, and quiet mornings with you.
Your love makes me grateful for all the roads that led me here.
I never need a special occasion to appreciate you.
You are my favorite reason to look forward to tomorrow.
I love the way we can laugh at things nobody else would understand.
You make the simplest moments feel like secret treasures.
I want to know your dreams, not just your habits.
Your happiness matters to me even when you do not ask.
I love that your presence can say more than a thousand messages.
You are the person I would choose when life stops being easy.
My heart found something rare in you, and I refuse to take it lightly.
I want our story to be made of small, honest moments.
You are the comfort I did not know I was searching for.
I love the peace that comes from knowing we choose each other.
I want to hold your hand through every unexpected chapter.
You make me feel seen without asking me to explain everything.
I would rather have your genuine smile than a room full of applause.
You are proof that love can arrive quietly.
I love you beyond the words I know how to say.
Your presence has become one of my favorite parts of life.
I want to keep learning the language of your heart.
You make me want to protect the little things that make us us.
I love that being with you never feels like performing.
You are my favorite person to do absolutely nothing with.
I want our love to feel like friendship that never stopped growing.
Even after ordinary days, I find new reasons to love you.
You make my heart believe that staying can be beautiful.
I would choose a lifetime of little moments with you over one perfect day.
You are not just part of my life; you are part of how I experience it.'''.splitlines()

cats['Sad']='''Sometimes the person you miss is the reason you hurt.
I smile because explaining the sadness feels harder.
Some memories arrive carrying more weight than they should.
I miss who you were before everything changed.
Not every broken heart makes a sound.
There are goodbyes the heart keeps replaying.
I stopped explaining because some people only listen to reply.
The hardest part was accepting that you were already gone.
Some nights feel longer because memories refuse to sleep.
I still have words I will never send.
I miss the days when your presence felt permanent.
Sometimes healing looks like pretending you are okay until you finally are.
You left, but the empty spaces remembered you.
I wish forgetting worked as easily as leaving.
Some people become strangers while their memories stay familiar.
I learned to hide heavy feelings behind ordinary conversations.
The heart often understands the ending after the mind does.
I do not hate you; I hate what we became.
There are questions I stopped asking because I already know the answer.
I still remember little things you probably forgot.
Some wounds are invisible because they live in memories.
I miss the version of us that never got a proper goodbye.
It hurts when someone becomes a memory before you are ready.
I have accepted the ending, but I still miss the beginning.
Sometimes silence is just sadness without a place to go.
I wish I could revisit the days before everything felt complicated.
The loneliest feeling is missing someone who has moved on.
I stopped waiting, but a small part of me still remembers.
Some memories feel beautiful until they suddenly hurt.
I learned that closure does not always arrive with an explanation.
I can forgive you and still remember what it cost me.
There are nights when being strong feels exhausting.
I miss the conversations we never got to finish.
Some endings leave questions instead of answers.
I wish I could tell my past self what I know now.
You can move forward and still carry a little sadness.
I am healing from things I never found the courage to name.
Sometimes the hardest goodbye is the one nobody says.
I stopped checking for messages, but I still notice the silence.
Some people leave footprints that time does not easily erase.
I wish memories came with an off switch.
I learned to cry quietly because not every pain needs an audience.
The saddest memories are often the happiest ones we can no longer repeat.
I still wonder if you ever think about the things we lost.
Some days I miss you; other days I miss who I was with you.
I am tired of pretending certain things never mattered.
There are feelings I buried because carrying them became too heavy.
Sometimes the heart wants an answer the past cannot give.
I thought time would erase everything, but it only taught me to carry it.
I do not want you back; I just want the memories to hurt less.
Some people leave quietly and change your life loudly.
I learned how to keep going with an unfinished story.
The hardest thing was accepting that love could not fix everything.
I miss being understood without having to explain myself.
Some memories return when the world becomes quiet.
I still remember how safe everything once felt.
There is a special kind of sadness in becoming strangers.
I wish we had known which moments were our last.
Sometimes the heart grieves people who are still alive but no longer yours.
I am okay, just not the same kind of okay as before.
The silence after losing someone can feel louder than an argument.
I stopped expecting apologies because healing had to begin without them.
Some pain fades slowly because it meant something deeply.
I miss the person I thought you would always be.
I learned that letting go can hurt even when it is necessary.
There are memories I keep because forgetting would feel like losing twice.
Sometimes you can be surrounded by people and still feel alone.
I wish I could tell you how different everything feels now.
Some nights, the past feels closer than the present.
I stopped blaming myself for an ending I could not control.
It is strange how someone can be gone and still appear everywhere.
I miss the comfort, not the confusion.
Some wounds heal quietly while the world thinks you moved on overnight.
I have made peace with the silence, even if I never wanted it.
The hardest lesson was learning that not everyone stays.
I remember enough to know why I had to leave.
Sometimes you mourn a future that never happened.
I wish the good memories did not come with such heavy feelings.
I learned to let tears exist without calling them weakness.
There are days when the smallest reminder changes my whole mood.
I am slowly becoming someone who can remember without breaking.
Some people are lessons that take years to understand.
I no longer chase what chose to leave me behind.
The heart can miss someone the mind knows it should release.
I stopped asking why and started asking what I learned.
There is courage in admitting that something still hurts.
I do not regret loving; I regret forgetting myself while doing it.
Some endings are painful because they were once beautiful.
I am learning that missing someone does not mean going back.
One day these memories will feel lighter than they do today.
I carry the lesson, not the bitterness.
I survived the days I thought would break me.
Maybe healing is simply remembering without wanting to return.'''.splitlines()

cats['Motivation']='''Keep going; your story is not finished yet.
Small steps still count when they move you forward.
Believe in yourself before waiting for anyone else to do it.
A difficult season does not mean a failed life.
Every struggle is teaching you something strength cannot learn easily.
You are allowed to start small and dream big.
Progress matters even when nobody notices it.
Your future deserves more effort than your excuses.
Do not quit during the chapter that is building you.
Some doors open only after you keep knocking.
Discipline carries you when motivation disappears.
The person you want to become is built by today's choices.
One bad day cannot cancel years of effort.
Your pace can be slow without being wrong.
Keep showing up for the life you say you want.
Failure is information, not an identity.
You do not need a perfect beginning to create a great ending.
Your comfort zone cannot introduce you to your full potential.
Hard days are not proof that you should stop.
Let your actions become louder than your doubts.
The dream is still possible, even if the route changed.
You have survived every difficult day that came before this one.
Consistency can turn ordinary effort into extraordinary results.
Start before you feel completely ready.
Your next breakthrough may be hiding behind one more attempt.
Do not compare your first step with someone else's tenth year.
Patience is part of the work, not a delay to it.
Keep learning until the things that scare you become familiar.
Your future self is counting on the choices you make today.
A setback can redirect you without defeating you.
The road gets easier when you stop arguing with the process.
You can rebuild from almost anything.
Your effort matters even when the result arrives late.
Do not let temporary discomfort decide your permanent future.
Courage is simply moving while fear is still present.
Every morning gives you another chance to improve.
Make progress your habit, not your occasional mood.
Your goals need action more than they need announcements.
Keep working when nobody is clapping.
One focused year can change more than you imagine.
The hardest part is often beginning again.
You are capable of learning what you do not know yet.
Do not confuse slow growth with no growth.
Your dream deserves a version of you who refuses to quit.
Work on yourself until your confidence has evidence behind it.
A quiet effort can create a loud future.
Do not wait for motivation to rescue your discipline.
You can be tired and still take one more step.
Every mistake can become useful if you learn from it.
Your circumstances can change when your habits change.
Keep your vision bigger than today's frustration.
Success often starts with doing the boring things consistently.
You do not need everyone's belief to begin.
The person who keeps going eventually passes the person who keeps waiting.
Make today useful, even if it is not perfect.
Your potential grows whenever you challenge your limits.
Do not let yesterday decide what today can become.
A new result often requires an old comfort to be left behind.
You are closer to becoming stronger than you think.
Let discipline finish what motivation started.
Your story can change with one brave decision.
Keep planting even when the season looks empty.
The work you do privately can change your life publicly.
Your excuses cannot build the future you imagine.
Be patient with the version of you that is still learning.
Every attempt makes the next attempt smarter.
You can restart without erasing everything you have learned.
Your dream does not need permission from people who fear it.
Choose progress over perfection every single day.
The struggle will not last forever, but the strength can.
Keep moving even when the destination feels far away.
You are not behind; you are building at your own pace.
Do not stop because the first results are small.
Your habits are quietly writing your future.
Make your next decision better than your last one.
A strong life is built from ordinary disciplined days.
You do not need to see the whole staircase to take the next step.
The best time to improve is the day you stop making excuses.
Your future can be different because your choices can be different.
Let your setbacks teach you instead of defining you.
You have more room to grow than your current limits suggest.
Keep your promises to yourself.
The life you want will require effort from the version of you you are today.
Do not fear being a beginner.
Your consistency will eventually become your advantage.
Every difficult day you handle becomes proof of your strength.
Stay focused while the world is busy distracting you.
You can do hard things without having all the answers.
Make resilience part of your routine.
Your dream becomes real one repeated action at a time.
Do not wait for confidence; build it through action.
Keep going until your doubt has nothing left to say.
Your best chapter may still be unwritten.
One day you will be grateful you refused to stop.'''.splitlines()

cats['Life']='''Life becomes richer when you notice the little things.
Not every chapter needs to make sense while you are living it.
There is no prize for rushing through your own life.
Sometimes losing something creates room for a better direction.
Peace is one of the quietest forms of success.
Life teaches lessons that no classroom can fully explain.
Ordinary moments often become precious after they are gone.
Growing up means learning what deserves your energy.
A different perspective can make the same life feel new.
Do not rush through moments you will someday miss.
Some people are chapters, not the entire story.
The best memories rarely arrive with a schedule.
Life feels lighter when gratitude becomes a daily habit.
You do not need everything figured out to move forward.
Some endings quietly make space for better beginnings.
Time reveals truths that conversations sometimes hide.
A peaceful life is not a boring life.
You can appreciate where you are while still wanting more.
The smallest joys are often the easiest to overlook.
Life changes when you stop measuring it against someone else's.
Not every delay is a denial; some are redirections.
Your current season is not your permanent address.
Sometimes the lesson is simply to let things be.
The people you love are part of what makes time meaningful.
Life is made of moments, not milestones alone.
You cannot control every event, but you can choose your response.
Some roads only make sense after you have walked them.
Happiness often hides inside ordinary routines.
There are seasons for building and seasons for resting.
Do not postpone living until everything feels perfect.
Time is precious because it never repeats itself.
Some goodbyes protect the life you are becoming.
A slow season can still be a meaningful season.
Life becomes calmer when expectations become realistic.
You are allowed to change the plans you once made.
Some people enter your life to teach, not to stay.
The present deserves attention because it will soon become memory.
Life is not a straight line; it is a collection of turns.
Sometimes getting lost helps you discover what matters.
The older you become, the more valuable peace feels.
A simple day can hold a beautiful memory.
Do not overlook the people who make normal days easier.
Life does not promise certainty, and that is part of its beauty.
You can begin again without calling the past a failure.
Every season has something to teach you.
Some things take longer because they are shaping you too.
The best parts of life cannot always be measured.
You do not need a perfect life to have meaningful days.
Let yourself enjoy the moment you are currently in.
Life becomes beautiful when comparison becomes gratitude.
Some memories are worth more than expensive things.
You can outgrow a place without hating what it once gave you.
The right pace is the one that lets you actually live.
Sometimes peace means accepting what you cannot change.
Your life deserves more attention than other people's timelines.
A difficult chapter does not ruin the whole book.
The people who stay during ordinary days are often the most valuable.
Life has a way of teaching patience through waiting.
Some answers arrive only after you stop forcing them.
The best moments are often too simple to plan.
You are allowed to enjoy life before everything is solved.
Change can be uncomfortable and still be necessary.
A meaningful life is built from small choices repeated over time.
Do not let temporary problems steal permanent moments.
There is beauty in becoming someone you did not expect to be.
Life feels different when you stop trying to control every outcome.
Sometimes walking away is how you protect your future.
The present is the only part of life you can actually hold.
Every person you meet leaves something behind: a memory or a lesson.
Some days are for achieving; others are for simply breathing.
Your story does not need to look like anyone else's.
A quiet life can still be a deeply successful one.
Do not forget to live while you are busy building.
Life gives meaning to the moments we choose to notice.
Some losses teach you what you were taking for granted.
You can miss the past without wanting to return to it.
The future is uncertain, but today is real.
Life gets lighter when you stop carrying what was never yours.
There is wisdom in knowing when enough is enough.
The people around you can change the way ordinary days feel.
A grateful heart notices what a restless mind overlooks.
Sometimes the best plan is to be present.
Your life is happening now, not someday.
Some seasons are quiet because growth is happening underneath.
You do not have to understand the whole journey to appreciate the view.
Life rewards patience in ways we often notice too late.
A meaningful life is not necessarily a loud one.
The older memories become, the more valuable the details feel.
Do not wait for a special day to appreciate an ordinary one.
Some chapters end because they have taught everything they came to teach.
Life becomes more peaceful when you stop forcing people to stay.
Every sunrise is a small reminder that beginnings are possible.
Your life can change without warning, so love the people you have today.
There is still beauty ahead that you have not met yet.
Make room for joy, even while you are figuring things out.
One day, today's ordinary moments may become your favorite memories.'''.splitlines()

cats['Self Love']='''I am learning to love myself without needing a reason.
I deserve the same kindness I keep giving to everyone else.
Choosing myself is not selfish when I have spent years forgetting myself.
My worth does not rise or fall with someone's opinion.
I am enough, even on days when I feel unfinished.
I am becoming a safe place for my own heart.
I will not abandon myself just to keep someone close.
My peace deserves protection.
I am proud of how far I have come, even if I still have miles to go.
I can choose myself without feeling guilty about it.
I deserve patience from the person I spend every day with: me.
My mistakes are part of my story, not the measure of my worth.
I am allowed to grow beyond the person I used to be.
I do not need applause to recognize my own progress.
My flaws do not cancel the good inside me.
I am allowed to rest without earning it first.
I can love who I am while still working on who I want to become.
My boundaries are one of the ways I care for myself.
I do not need to shrink so other people can feel comfortable.
I am learning to enjoy my own company.
My past deserves compassion, not endless punishment.
I deserve relationships that feel safe, honest, and mutual.
I am more than the mistakes I made while learning.
I can say no without explaining my entire heart.
My happiness matters even when nobody else notices it.
I am becoming someone I can trust.
I no longer measure my worth by how useful I am to others.
I deserve the life I am patiently building.
I can forgive myself for not knowing then what I know now.
My healing does not need a deadline.
I am allowed to protect my energy.
I do not need to be perfect to be lovable.
I can leave what hurts me without hating myself for staying before.
My value remains even when someone chooses not to see it.
I am learning to speak to myself with the same softness I offer others.
I deserve peaceful mornings and quiet nights.
I do not need everyone to understand my choices.
I am allowed to outgrow old versions of myself.
My self-respect is more important than being universally liked.
I can be a work in progress and still be worthy today.
I am learning to celebrate small victories.
I trust myself a little more every time I keep a promise to myself.
I do not have to earn rest by breaking myself first.
My heart deserves gentleness after everything it has carried.
I am not behind; I am becoming.
I can start over without calling myself a failure.
My happiness is not something I have to apologize for.
I am worthy on my productive days and my quiet days.
I do not need someone else to complete the parts of me I am learning to love.
I am allowed to choose peace over people-pleasing.
My voice deserves to be heard, including by me.
I can be strong without becoming hard.
I deserve to feel at home in my own skin.
I am learning that solitude can be peaceful, not lonely.
My journey deserves respect even when it looks different from others.
I am not responsible for carrying everyone's emotions.
I choose authenticity over approval.
I deserve honesty from others and kindness from myself.
I am proud of every version of me that kept going.
I can release what no longer fits without questioning my worth.
My boundaries are not walls; they are doors with conditions.
I do not need to prove that I deserve love.
I am allowed to take up space in my own life.
My peace is not a luxury; it is a necessity.
I am learning to trust my instincts again.
I deserve to be celebrated by myself too.
I do not need to compare my chapter with anyone else's.
I can be gentle with myself while still holding myself accountable.
My identity is bigger than anyone's rejection.
I choose growth because I believe I am worth the effort.
I am allowed to change my mind when something no longer feels right.
I deserve friendships that do not require me to perform.
I am learning to stop chasing acceptance.
My heart does not need to apologize for needing care.
I can love myself without waiting to become perfect.
I deserve a life that does not constantly drain me.
I am becoming the person I once needed.
I will not use someone else's standards to measure my soul.
My progress counts even when it is invisible to others.
I am allowed to celebrate myself without feeling arrogant.
I can protect my peace without closing my heart.
I deserve a future that feels like mine.
I am learning that saying no can be an act of love toward myself.
My worth is not negotiable.
I can forgive myself and still choose better next time.
I deserve to feel proud when I look at the person I am becoming.
I am not my worst day.
I am not too much for the right people.
I am allowed to leave spaces where I constantly have to prove my value.
My happiness begins with how I treat myself when nobody is watching.
I deserve the same grace I give to people I love.
I am learning to stop abandoning my needs for someone else's comfort.
I can be independent without pretending I never need support.
I choose myself because I finally understand my own value.
I am worthy before I achieve anything.
I am allowed to heal at my own pace.
The relationship with myself deserves daily attention.
I will keep choosing the version of me that feels honest and free.'''.splitlines()

cats['Success']='''Success begins when excuses stop making decisions for you.
Work quietly until your results have their own voice.
A dream becomes useful when you give it a plan.
Consistency can take you places motivation cannot.
The hardest work is often the work nobody sees.
Your effort today can become your freedom tomorrow.
Build yourself into the person who can handle the success you want.
Small progress becomes powerful when it never stops.
Discipline turns intentions into evidence.
A successful life is built on ordinary days done well.
Keep showing up, especially when the excitement fades.
Your habits are voting for the future you will eventually live.
Do not wait for the perfect opportunity; prepare for it.
Success is rarely sudden; it is usually accumulated.
Your first goal should be becoming better at what you do.
One focused year can change the direction of a life.
Do not confuse movement with meaningful progress.
The work you avoid may be the skill you most need.
Your future deserves today's uncomfortable decisions.
A setback can become useful if you refuse to waste the lesson.
Success requires patience because foundations take time.
Build skills that make opportunities easier to recognize.
You do not need to be the fastest; you need to remain consistent.
The people who win long-term learn to love the process.
Your competition is yesterday's version of you.
Do the small things well enough and they become big things.
A strong career is built long before the title arrives.
Your results eventually reveal your routines.
Do not chase applause; chase mastery.
The best investment is becoming harder to replace.
Success grows where discipline is stronger than mood.
Your goals need calendars, not just wishes.
Keep learning after the first success; that is how you keep it.
The road gets clearer when you take the next step.
You can change your future by changing what you repeat.
Hard work without direction is noise; work with purpose.
Make your standards higher than your excuses.
Your next level will require habits your current level does not.
Do not stop because the first result is small.
Every expert has a history of being a beginner.
Success often looks boring before it looks impressive.
Focus is a competitive advantage in a distracted world.
The work you do when nobody cares is what prepares you for when they do.
Your dream deserves more than occasional effort.
Do not let temporary comfort become a permanent ceiling.
A clear goal makes difficult days easier to navigate.
Keep improving the skill that creates your value.
Your future is being built by what you repeat today.
Success is often a collection of small promises kept.
Learn to enjoy progress before you reach the finish line.
Do not measure your journey only by visible results.
Patience protects good work from being abandoned too early.
The strongest businesses, careers, and lives are built on consistency.
Your opportunity may arrive after the moment you wanted to quit.
Preparation makes luck more useful.
Do not wait for confidence; let action create it.
A disciplined hour today can save months tomorrow.
Your potential means little until you put it into practice.
Keep your standards when nobody is watching.
Success is easier to sustain when it is built on character.
Make decisions your future self will respect.
Do not compare your beginning with someone else's established life.
Your pace matters less than your direction.
A difficult goal becomes manageable when broken into daily actions.
Work until your skills can speak for you.
Do not fear starting small; fear staying stuck.
Your habits can change your income, your confidence, and your options.
Success is not just reaching the goal; it is becoming capable along the way.
Build something that keeps working after motivation disappears.
The strongest advantage is the ability to keep learning.
Your next breakthrough may require one more uncomfortable attempt.
Do not let one failure become a permanent conclusion.
The future rewards people who prepare before they are noticed.
Stay focused while others are distracted by shortcuts.
Your work compounds when you keep improving it.
A slow climb is still a climb.
Do not sacrifice your long-term future for short-term comfort.
Your reputation is built through repeated actions, not one big moment.
The best time to become serious about your goals is before regret arrives.
Success asks for consistency long after excitement has left.
Create systems that make progress easier to repeat.
You cannot control every result, but you can control the quality of your effort.
Keep your vision clear when the path becomes messy.
A strong foundation makes future growth less fragile.
Do not spend more time announcing goals than working on them.
Your best opportunity may be the skill you have not mastered yet.
Every difficult project teaches you something valuable.
Success becomes sustainable when discipline becomes normal.
Keep going until the work you once feared becomes routine.
The goal is not to look successful; it is to become capable.
Your future can be built one focused decision at a time.
Do not underestimate the power of showing up every day.
The gap between wishing and achieving is filled with action.
Build quietly, learn constantly, and improve deliberately.
One day, the sacrifices behind your success will explain the result.'''.splitlines()

extras={
'Attitude':['I choose my standards over someone else’s expectations.'],
'Love':['You are the kind of person I would choose in both the easy days and the hard ones.','Somewhere in your presence, my heart learned what comfort feels like.','I want our love to remain honest even when life is not easy.'],
'Sad':['I am learning to carry the memory without carrying the pain.','Sometimes healing begins when you stop pretending it never hurt.','I wish some memories came with softer endings.','There are days when I am fine until one song changes everything.','I learned that missing someone and needing them are not the same thing.','Some feelings stay quiet because words would make them heavier.','I am slowly making peace with a story I never wanted to end.'],
'Motivation':['Your effort may be invisible today, but it is not meaningless.','Keep choosing the next right step instead of fearing the whole journey.','You do not need a miracle when you are willing to keep working.','Let your patience be as strong as your ambition.','Your discipline can carry you farther than temporary inspiration.','The future changes when ordinary choices become intentional.'],
'Life':['Some of the best parts of life arrive without an announcement.','A good life is often quieter than the life people show online.','You can be grateful for yesterday and still be excited about tomorrow.','Sometimes the most important journey is the one back to yourself.'],
'Self Love':['I deserve to speak to myself without cruelty.','My needs are allowed to matter in my own story.'],
'Success':['Make your work so useful that opportunities begin looking for you.','Long-term success is often built by people who can stay patient when nobody is impressed.','Your discipline becomes an asset when your circumstances change.','The best results come from work that survives your changing moods.','Keep building the skill that your future opportunities will require.']}
for k,v in extras.items(): cats[k].extend(v)
assert all(len(v)==100 for v in cats.values()), {k:len(v) for k,v in cats.items()}
# Interleave categories only for All; category filter keeps category order. Ensure no duplicates.
assert len(set(sum(cats.values(),[])))==700
# write JS
out=['const quotes = [']
for cat, qs in cats.items():
    for q in qs:
        out.append('  '+json.dumps([cat,q],ensure_ascii=False)+',')
out.append('];')
# preserve remainder of script after old quotes array
old=open('/mnt/data/capwork/script.js').read()
end=old.find('];')
rest=old[end+2:]
open('/mnt/data/capwork/script.js','w').write('\n'.join(out)+rest)
print('written', sum(map(len,cats.values())))
