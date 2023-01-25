from collections import defaultdict

def solution(streamerInformation, commands):
    streamers = dict()
    categories = defaultdict(set)
    response = list()
    
    for i in range(0, len(streamerInformation), 3):
        name = streamerInformation[i]
        numviews = streamerInformation[i + 1]
        category = streamerInformation[i + 2]
        
        streamers[name] = [numviews, category]
        categories[category].add(name)

    print(streamers)
        
    i = 0
    while i < len(commands):
        if commands[i] == 'StreamerOnline':
            name = commands[i + 1]
            numviews = commands[i + 2]
            category = commands[i + 3]
            
            streamers[name] = (numviews, category)
            categories[category].add(name)
            i += 4
            
        elif commands[i] == 'UpdateViews':
            name = commands[i + 1]
            numviews = commands[i + 2]
            category = commands[i + 3]
            
            if name in streamers and streamers[name][1] == category:
                streamers[name][0] = numviews
                
            i += 4
            
        elif commands[i] == 'UpdateCategory':
            name = commands[i + 1]
            category = commands[i + 2]
            new_category = commands[i + 3]
            
            if name in streamers and streamers[name][1] == category:
                streamers[name][1] = new_category
                
                categories[category].remove(name)
                categories[new_category].add(name)
                
            i += 4
            
        elif commands[i] == 'StreamerOffline':
            name = commands[i + 1]
            category = commands[i + 2]
            
            if name in streamers and name in categories[category]:
                streamers.pop(name)
                categories[category].remove(name)
                
            i += 3
            
        elif commands[i] == 'ViewsInCategory':
            category = commands[i + 1]
            
            if not category in categories:
                response.append(0)
                
            else:
                total_views = 0
                
                for streamer in categories[category]:
                    total_views += int(streamers[streamer][0])
                    
                response.append(str(total_views))
                
            i += 2
            
        elif commands[i] == 'TopStreamerInCategory':
            category = commands[i + 1]
            
            if not category in categories or len(categories[category]) == 0:
                response.append(None)
                
            else:
                max_streamer = ''
                
                for streamer in categories[category]:
                    if max_streamer == '':
                        max_streamer = streamer
                        continue
                        
                    views = int(streamers[streamer][0])
                    
                    if views > int(streamers[max_streamer][0]):
                        max_streamer = streamer
                    
                response.append(max_streamer)
                
            i += 2
            
        elif commands[i] == 'TopStreamer':
            if len(streamers) == 0:
                response.append(None)
                continue
                
            max_streamer = ''
            
            for streamer in streamers:
                if max_streamer == '':
                    max_streamer = streamer
                    continue
                    
                views = int(streamers[streamer][0])
                
                if views > int(streamers[max_streamer][0]):
                    max_streamer = streamer
                    
            response.append(max_streamer)
            
            i += 1

        else:
            i += 1
            
    return response

#Custom Testing
print(solution(
    ['Ninja', 3000, 'Gaming', 
    'Boi3', 2000, 'Gaming', 
    'John', 300000, 'Hot Tub',
    'XQC', 400000, 'Vlogs'],
    ['TopStreamer', 
    'TopStreamerInCategory', 'Gaming',
    'ViewsInCategory', 'Gaming']
))