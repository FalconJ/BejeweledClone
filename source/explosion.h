#if !defined(__EXPLOSION_H__)
#define __EXPLOSION_H__

#include <list>
#include "Iw2DSceneGraph.h"

using namespace Iw2DSceneGraphCore;
using namespace Iw2DSceneGraph;


class Explosion : public CSprite
{
protected:
    bool        InUse;
public:
    bool        isInUse() const         { return InUse; }
    void        setUsed(bool used)      { InUse = used; }
public:
    Explosion();
    ~Explosion()        {}

    void        Update(float deltaTime, float alphaMul);

};

class ExplosionManager
{
protected:
    std::list<Explosion*>       Explosions; // Explosions list

public:
    Explosion*      Create(float x, float y);
    void            ReleaseAll();

    ~ExplosionManager();

};

extern ExplosionManager*    g_pExplosionManager;


#endif  // __GEM_H__


